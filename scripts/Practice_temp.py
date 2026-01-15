# %%
while True:
    emotion = str(input("User's Emotion: ")).strip().lower()

    if "lost" in emotion:
        print(f"Best solution for your emotion:- {emotion} - is Meditation for 15 min")
    elif "overthinking" in emotion:
        print(
            f"Best solution for your emotion:- {emotion} - is Dance for 10-15 min, followed by relaxation for 15 min"
        )
    elif "fear" in emotion:
        print(
            f"Best solution for your emotion:- {emotion} - is belly breathing for 5 min, with emphasis on exhale"
        )
    else:
        print(f"I can not help you in this emotion - {emotion}")
# %%
