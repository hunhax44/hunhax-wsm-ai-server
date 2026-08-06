import argostranslate.translate


def get_installed_languages():
    return argostranslate.translate.get_installed_languages()


def translate(text, source_code, target_code):

    installed_languages = get_installed_languages()

    from_lang = next(
        (
            lang
            for lang in installed_languages
            if lang.code == source_code
        ),
        None
    )

    to_lang = next(
        (
            lang
            for lang in installed_languages
            if lang.code == target_code
        ),
        None
    )

    if not from_lang:
        raise Exception(
            f"Language not installed: {source_code}"
        )

    if not to_lang:
        raise Exception(
            f"Language not installed: {target_code}"
        )

    translation = from_lang.get_translation(to_lang)

    return translation.translate(text)
