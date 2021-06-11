from ie_utils import tokenize
import sys
import click

@click.command()
@click.option('--sentence',prompt='Write your sentence', default='Hello World')

def main(sentence):
    """IE Tokenizer"""
    print(tokenize(sentence))


if __name__ == "__main__":
    print(main())

    
    

#def main():
#    print(tokenize(sys.argv[1]))



#print(tokenize("Hello World!"))




