import string
import math

def password_strength(password):
    length = len(password)
    
    # Character type flags
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    
    # Character pool size
    pool = 0
    pool += 26 if has_lower else 0
    pool += 26 if has_upper else 0
    pool += 10 if has_digit else 0
    pool += len(string.punctuation) if has_symbol else 0
    
    # Entropy calculation
    entropy = length * math.log2(pool) if pool > 0 else 0
    
    # Strength rating
    if entropy < 28:
        rating = "🔴 Very Weak"
    elif entropy < 36:
        rating = "🟠 Weak"
    elif entropy < 60:
        rating = "🟡 Moderate"
    elif entropy < 80:
        rating = "🟢 Strong"
    else:
        rating = "🔵 Very Strong"
    
    # Brute-force time estimate (assuming 10^9 guesses/sec)
    guesses_per_sec = 1_000_000_000
    total_combinations = pool ** length
    seconds = total_combinations / guesses_per_sec
    years = seconds / (60 * 60 * 24 * 365.25)
    
    return {
        "📏 Length": length,
        "🔠 Character Types": {
            "Lowercase": has_lower,
            "Uppercase": has_upper,
            "Digits": has_digit,
            "Symbols": has_symbol
        },
        "🎲 Pool Size": pool,
        "🧠 Entropy (bits)": round(entropy, 2),
        "🛡️ Strength Rating": rating,
        "⏳ Estimated Crack Time": {
            "Seconds": f"{seconds:,.0f} seconds",
            "Years": f"{years:,.2f} years (at 10⁹ guesses/sec)"
        }
    }

# Example usage
pwd = "12345678"
result = password_strength(pwd)

print("\n🔐 PASSWORD STRENGTH REPORT")
print("════════════════════════════")
for k, v in result.items():
    if isinstance(v, dict):
        print(f"{k}:")
        for sub_k, sub_v in v.items():
            print(f"  - {sub_k}: {'✅' if sub_v is True else '❌' if sub_v is False else sub_v}")
    else:
        print(f"{k}: {v}")
print("════════════════════════════\n")
