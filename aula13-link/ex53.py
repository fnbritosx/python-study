phrase = input('Type a sentence: ').strip().lower()
phrase = ''.join(c for c in phrase if c.isalnum())  

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if is_palindrome(phrase):
    print('É palíndromo!')
else:
    print('Não é palíndromo.')

