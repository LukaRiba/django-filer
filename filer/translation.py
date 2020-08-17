from modeltranslation.translator import translator, TranslationOptions

from filer.models.filemodels import File
from filer.models.imagemodels import Image



class FileTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


class ImageTranslationOptions(TranslationOptions):
    fields = ('default_alt_text', 'default_caption',)

translator.register(File, FileTranslationOptions)
translator.register(Image, ImageTranslationOptions)