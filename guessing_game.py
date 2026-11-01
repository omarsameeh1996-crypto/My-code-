"""لعبة تخمين الرقم.

يختار البرنامج رقمًا عشوائيًا من 1 إلى 100، ويطلب من المستخدم تخمينه،
ويخبره إذا كان الرقم المطلوب أعلى أو أقل، ويحسب عدد المحاولات حتى يفوز.
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 100


def read_guess():
    """يقرأ تخمينًا صحيحًا من المستخدم ضمن النطاق المسموح."""
    while True:
        text = input(f"أدخل تخمينك ({MIN_NUMBER}-{MAX_NUMBER}): ").strip()
        try:
            guess = int(text)
        except ValueError:
            print("⚠️  من فضلك أدخل رقمًا صحيحًا.")
            continue
        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print(f"⚠️  الرقم يجب أن يكون بين {MIN_NUMBER} و {MAX_NUMBER}.")
            continue
        return guess


def play():
    """تشغيل جولة واحدة من اللعبة."""
    secret = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0

    print(f"\n🎲 اخترت رقمًا بين {MIN_NUMBER} و {MAX_NUMBER}. حاول تخمينه!")

    while True:
        guess = read_guess()
        attempts += 1

        if guess < secret:
            print("⬆️  الرقم أعلى من تخمينك.")
        elif guess > secret:
            print("⬇️  الرقم أقل من تخمينك.")
        else:
            print(f"🎉 مبروك! الرقم هو {secret}. فزت بعد {attempts} محاولة.")
            return attempts


def main():
    print("=== لعبة تخمين الرقم ===")
    try:
        while True:
            play()
            again = input("\nهل تريد اللعب مرة أخرى؟ (نعم/لا): ").strip().lower()
            if again not in ("نعم", "ن", "y", "yes"):
                print("شكرًا على اللعب! 👋")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nتم إنهاء اللعبة. إلى اللقاء! 👋")


if __name__ == "__main__":
    main()
