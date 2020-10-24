import spacy

from typing import Dict, Generator, Iterable, Optional, Sequence, Union

from .base import Detector
from ..filth import NamedEntityFilth, Filth
from ..utils import CanonicalStringSet


class NamedEntityDetector(Detector):
    """Use spacy's named entity recognition to clean named entities.
     List specific entities to include passing ``named_entities``, e.g.
     (PERSON)
    """
    filth_cls = NamedEntityFilth
    name = 'named_entity'

    disallowed_nouns = CanonicalStringSet(["skype"])

    def __init__(self, named_entities: Iterable[str] = {'PERSON'},
                 model: str = "en_core_web_trf", **kwargs):
        # Spacy NER are all upper cased
        self.named_entities = {entity.upper() for entity in named_entities}
        if model not in spacy.info()['pipelines']:
            raise OSError("Can't find model '{}'. If it is a valid Spacy model, "
                          "download it (e.g. with the CLI command "
                          "`python -m spacy download {}`).".format(model, model))
        self.nlp = spacy.load(model)
        # Only enable necessary pipes
        self.nlp.select_pipes(enable=["transformer", "tagger", "parser", "ner"])
        super(NamedEntityDetector, self).__init__(**kwargs)

    def _iter_spacy_pipeline(self, doc_names: Sequence[Optional[str]], doc_list: Sequence[str]):
        for doc_name, doc in zip(doc_names, self.nlp.pipe(doc_list)):
            for ent in doc.ents:
                if ent.label_ in self.named_entities:
                    yield self.filth_cls(beg=ent.start_char,
                                         end=ent.end_char,
                                         text=ent.text,
                                         document_name=None or str(doc_name),  # None if no doc_name provided
                                         detector_name=self.name,
                                         label=ent.label_)

    def iter_filth_documents(self, documents: Union[Sequence[str], Dict[str, str]]) -> Generator[Filth, None, None]:
        if isinstance(documents, list):
            doc_names, doc_list = zip(*enumerate(documents))
        elif isinstance(documents, dict):
            doc_names, doc_list = zip(*documents.items())
        else:
            raise TypeError('documents must be one of a string, list of strings or dict of strings.')

        yield from self._iter_spacy_pipeline(doc_names, doc_list)

    def iter_filth(self, text: str, document_name: Optional[str] = None) -> Generator[Filth, None, None]:
        yield from self._iter_spacy_pipeline([document_name], [text])