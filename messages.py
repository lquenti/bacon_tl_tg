import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(BASE_DIR, "static")

BASE_URL = "http://lquenti.de/bacon_pictures/"

ALL_MESSAGES = [
    "Just wrapped my timeline in 3 ½ feet of bacon. http://LittleCaesarsBaconTimeline.com",
    "Inch two of 3 ½ feet of bacon.",
    "Inch three of 3 ½ feet.",
    "Fourth inch of a @LittleCaesars 3 ½ foot strip of bacon.",
    "Inch five of 3 ½ feet of bacon.",
    "Keep scrolling. We wrap our pizza in a lot of bacon.",
    "Inch seven of 3 ½ feet.",
    "Inch eight...",
    "Inch nine of Little Caesars Bacon Timeline.",
    "Inch ten.",
    "Inch eleven.",
    "Only 2 ½ feet of Little Caesars bacon to go.",
    "Inch thirteen of 3 ½ feet.",
    "Inch fourteen of a Little Caesars strip of bacon.",
    "Inch fifteen...",
    "You guessed it, inch sixteen.",  # 119 Retweets 49 Likes lol
    "We wrap our pizza in a pretty long strip of bacon huh?",
    "Inch eighteen.",
    "Here’s inch nineteen...",
    "Inch twenty of 3 ½ feet.",
    "The @LittleCaesars Bacon Timeline halfway point.",
    "This is inch twenty-two.",
    "Inch twenty-three.",
    "Inch twenty-four of a Little Caesars strip of bacon.",
    "Inch twenty-five of 3 ½ feet.",
    "Inch twenty-six.",
    "Inch twenty-seven on your timeline courtesy of Little Caesars.",
    "Inch twenty-eight of 3 ½ feet.",
    "And we’re done!",
    "Just kidding. More @LittleCaesars Bacon Timeline.",
    "Inch thirty-one of 3 ½ feet of bacon.",
    "Inch thirty-two of 3 ½ feet.",
    "Official Little C’s thirty-third inch.",
    "Inch thirty-four of 3 ½ feet.",
    "Inch thirty-five...",
    "Still the same strip of bacon we use on our pizza. Almost there.",
    "Inch thirty-seven of 3 ½ feet.",
    "Inch thirty-eight.",
    "Inch thirty-nine of Little Caesars Bacon Timeline.",
    "Inch forty of 3 ½ feet of bacon.",
    "Inch forty-one of 3 ½ feet of bacon.",
    "End of @LittleCaesars Bacon Timeline. Time to enjoy the real thing at a location nearest you."
]

# https://t.me/addstickers/bacon_timeline
ALL_STICKER_IDS = [
    "CAACAgIAAxkBAAEBPGFfQBWsChKW2p_YLRVK9A8e6yC_TAACdQADzQUpCSai3vV53IPbGwQ",
    "CAACAgIAAxkBAAEBPH1fQBaUzUNXlQv61X_qGB7Gfs9U8QACdgADzQUpCbtNiDkxPc9oGwQ",
    "CAACAgIAAxkBAAEBPIFfQBax6Ufm_wrxVzdyn444FtSvBwACdwADzQUpCZnbKd2zij0jGwQ",
    "CAACAgIAAxkBAAEBPINfQBa-Pd9oVrJ-iKI90AXhqqQJyAACeAADzQUpCdjyJumiHe4HGwQ",
    "CAACAgIAAxkBAAEBPIVfQBbKRG0tMgcWu0v9iYSLrQj1JgACeQADzQUpCe4eSy4F6H98GwQ",  # 5

    "CAACAgIAAxkBAAEBPItfQBcIs8kuReGoachSCyMrtmo8oAACegADzQUpCQpYeqlUpE9xGwQ",
    "CAACAgIAAxkBAAEBPI1fQBcUjBTtoWxSvP4l4XGjQiaIjgACewADzQUpCfuWU2EUyJHSGwQ",
    "CAACAgIAAxkBAAEBPI9fQBceCP3xoTx0SovkoobpXW6W5gACfAADzQUpCfyb_3bCbRCBGwQ",
    "CAACAgIAAxkBAAEBPJFfQBcqqJEon9lmY98RlCRBjsd2PAACfQADzQUpCWKe751sq0kIGwQ",
    "CAACAgIAAxkBAAEBPJNfQBc1M6duslDBPRISSCfxkIJCUwACfgADzQUpCQW-ZGLVpF4VGwQ",

    "CAACAgIAAxkBAAEBPJVfQBdHCZiGf6z9Tzo7QXjNuRZpQwACfwADzQUpCTgKsjXESBrRGwQ",
    "CAACAgIAAxkBAAEBPJdfQBdT3pU0eKcv1K63NV_miIEmqgACgAADzQUpCevzO3Wn9-MGGwQ",
    "CAACAgIAAxkBAAEBPJlfQBdk7Wk3_byemAwx8FX1P-BuEAACgQADzQUpCc8hShoKOQ6AGwQ",
    "CAACAgIAAxkBAAEBPJtfQBd6--BL9hYF8oIOVbI7rBBTDAACggADzQUpCbmrrh10muGGGwQ",
    "CAACAgIAAxkBAAEBPJ1fQBd9U4Kg7cfpo0yQ79Ejn6as_gACgwADzQUpCReLqhaF9TltGwQ",  # 15

    "CAACAgIAAxkBAAEBPJ9fQBeA0zu6HNTRFkkxZOpqz6IingAChAADzQUpCQwddVjzzCn0GwQ",  # You guessed it
    "CAACAgIAAxkBAAEBPKdfQBey0rQ2SP8bDrO97Osh1jvNSAAChQADzQUpCfYPwp-uek8sGwQ",
    "CAACAgIAAxkBAAEBPKlfQBe1C4_PWHMSNVe2T-f6qBtBUQAChgADzQUpCSpk3iHcGkbEGwQ",
    "CAACAgIAAxkBAAEBPKtfQBe4zE7osCsRI0ydrhyfsOrBGQAChwADzQUpCaCuvLlTe6UhGwQ",
    "CAACAgIAAxkBAAEBPK1fQBe7vToilZWSqoRbMhe8Ju26ugACiAADzQUpCc9zwBax3LRAGwQ",  # 20

    "CAACAgIAAxkBAAEBPK9fQBe_GfHAUJ8DIwgEblR8CQptjwACiQADzQUpCXHp20WcmE6uGwQ",
    "CAACAgIAAxkBAAEBPLFfQBfBCy5mJo8dTJPdsL3L8-D8GgACigADzQUpCcvQ4RMPLHEoGwQ",
    "CAACAgIAAxkBAAEBPLNfQBfEOei9UT0cUhJ3aTrqAhgtoAACiwADzQUpCStLEDVQDuj2GwQ",
    "CAACAgIAAxkBAAEBPLVfQBfIMrh7l_r7ZzAFnurMSGWQvAACjAADzQUpCU-M-HiYkNmPGwQ",
    "CAACAgIAAxkBAAEBPLdfQBfOruU0bPdF-1UezvClk63XggACjQADzQUpCcN23nPv-oycGwQ",  # 25

    "CAACAgIAAxkBAAEBPLlfQBfStUDMSSlMYDrlqrcMmMKyPgACjgADzQUpCaqsRBDxwtCnGwQ",
    "CAACAgIAAxkBAAEBPLtfQBfVuQFVdtyKIo8dhOAQRnlXSwACjwADzQUpCZ8sFmKrcNpBGwQ",  # Funny man
    "CAACAgIAAxkBAAEBPL1fQBfkemifpU4Uc4qEtrI8_4CCaAACkAADzQUpCU2vMhw4nOVAGwQ",
    "CAACAgIAAxkBAAEBPL9fQBfmk_4Savmz82WHN-hKHnfzKwACkQADzQUpCT8ZNKvb8L-rGwQ",
    "CAACAgIAAxkBAAEBPMFfQBfp4hZvO13X9TbLjUKVrynoUQACkgADzQUpCen_jt1PuHM5GwQ",  # 30

    "CAACAgIAAxkBAAEBPMNfQBfsDbes-80XAtNiwmUeHSNEUgACkwADzQUpCWluJwjkRshPGwQ",
    "CAACAgIAAxkBAAEBPMVfQBfvxjo_l3O-Ai7O2IVHyZLquQAClAADzQUpCfihMu79lq1hGwQ",
    "CAACAgIAAxkBAAEBPMdfQBfxhndfUnrH07-mrqxgFjBuWwAClQADzQUpCXaei215QOdkGwQ",
    "CAACAgIAAxkBAAEBPMlfQBf0Y-750FysrSWh-LmEuGqEPQAClgADzQUpCdUu2fBebZgwGwQ",
    "CAACAgIAAxkBAAEBPMtfQBf3nhC1odV45DG6Rhsjtf5VdQAClwADzQUpCdJxbHbDQvSkGwQ",  # 35

    "CAACAgIAAxkBAAEBPM1fQBf6bWdWrKOSeatd7v6C3BiSmQACmAADzQUpCXntCoNTA0GUGwQ",
    "CAACAgIAAxkBAAEBPM9fQBf9sm8Bh_PWWNOmHQLgfGkuywACmQADzQUpCUK7EtacQVhgGwQ",
    "CAACAgIAAxkBAAEBPNFfQBgAAYQgO56dLRtFuMMEMNg7Gq8AApoAA80FKQkrMKS5m4EHrhsE",
    "CAACAgIAAxkBAAEBPNNfQBgCAYdg1KkOOBr7JZqf6CcoxQACmwADzQUpCcFYXs9v5dt0GwQ",
    "CAACAgIAAxkBAAEBPNVfQBgFQd0tNQ8MuNaMj1FUJvTFnAACnAADzQUpCdtX_3WyjXKNGwQ",  # 40

    "CAACAgIAAxkBAAEBPNdfQBgJVhNazw72GFSWTmXLB6Z9qQACnQADzQUpCaH4aLhcuXAAARsE",
    "CAACAgIAAxkBAAEBPNlfQBgM2ZNTrHXiL62K_sUKBbPYrwACngADzQUpCY9onrzSf9YTGwQ"
]


def __make_abs_paths(n: int):
    filename = "{}.jpeg".format(n)
    return os.path.join(STATIC_PATH, filename)


ALL_TWEETS_LINK = ["{}\n{}{}.jpg".format(msg, BASE_URL, index + 1) for index, msg in enumerate(ALL_MESSAGES)]
ALL_TWEETS_PIC = [(__make_abs_paths(index + 1), msg) for index, msg in enumerate(ALL_MESSAGES)]

ALL_TWEETS_STICKER = [*zip(ALL_STICKER_IDS, ALL_MESSAGES)]

START_MESSAGE = r"Sup, just type /bacon whenever you feel like it"
