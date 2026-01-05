while True:
    testpass = input("Enter your Password (or 'quit' to exit): ")
    
    if testpass.lower() == "quit":
        print("Thanks for using the password checker!")
        break
    
    pass_hasupper = False
    pass_haslower = False
    pass_hasnum = False
    pass_hasp = False
    
    for char in testpass:
        if char.isupper():
            pass_hasupper = True
        if char.islower():
            pass_haslower = True
        if char.isdigit():
            pass_hasnum = True
        if not char.isalnum() and not char.isspace():
            pass_hasp = True
    
    if pass_hasupper:
        print("✓ Has Uppercase")
    else:
        print("✗ Missing Uppercase")
    if pass_haslower:
        print("✓ Has Lowercase")
    else:
        print("✗ Missing Lowercase")
    if pass_hasnum:
        print("✓ Has Number")
    else:
        print("✗ Missing Number")
    if pass_hasp:
        print("✓ Has Special Letter")
    else:
        print("✗ Missing Speical letter")
    if len(testpass) >= 8:
        print("✓ Has 8+ Letters")
    else:
        print("✗ Too Short || Should be 8 letter or more")
    
    score = pass_hasupper + pass_haslower + pass_hasnum + pass_hasp + (len(testpass) >= 8)
    print(f"\nScore: {score}/5")
    
    if score <= 2:
        print("Password Strength: WEAK")
    elif score <= 4:
        print("Password Strength: MEDIUM")
    else:
        print("Password Strength: STRONG")
    
    common_passwords = ["password", "123456", "admin", "welcome", "qwerty"]
    if testpass.lower() in common_passwords:
        print("⚠️ This is a commonly used password - avoid it!")
    
    print("\n💡 Tips for a stronger password:")
    print("• Consider using a passphrase: 4+ random words or a memorable phrase")
    print("• Longer is better than complex - aim for 15+ characters")
    print("• Avoid personal info that's on social media (names, birthdays, pets)")
    print("\n" + "="*50 + "\n")