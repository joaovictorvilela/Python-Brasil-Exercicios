def main():

    nome = str(input('Digite: ')).upper().strip()
    alfabeto = {'A': '4','B': '8','C': '<','D': '[)','E': '&','F': 'ph','G': '6','H': '#','I': '1','J': 'j','K': '|<','L': '|_','M': '|\/|','N': '/\/','O': '0','P': '|*','Q': '9','R': 'l2','S': '5','T': '7','U': 'v','V': 'V','W': 'vv','X': '><','Y': '`/','Z': '2'}

    alfa = ''
    outros = ''

    for caractere in nome:
        if caractere.isalpha():
            alfa += alfabeto[caractere]
        else:
            outros += caractere

    print(outros + alfa)

main()

