from injection import xss
import argparse
import os


def main():
    parser = argparse.ArgumentParser(
        description='''
                                         88888b.d88888                   
              888  888 .d8888b  .d8888b  888Y88888P888  8888b.  88888b.  
              `Y8bd8P' 88K      88K      888 Y888P 888     "88b 888 "88b 
                X88K   "Y8888b. "Y8888b. 888  Y8P  888 .d888888 888  888 
              .d8""8b.      X88      X88 888   "   888 888  888 888  888 
              888  888  88888P'  88888P' 888       888 "Y888888 888  888 

    Injection tool for testing vulnerabilities.
    Usage: injection.py -u [URL] -i [Input ID] -b [Button Value] -l [XSS Payload]
            ''',
        formatter_class=argparse.RawTextHelpFormatter,
        usage=argparse.SUPPRESS
    )

    # Add arguments
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("-i", "--input_id", required=True, help="Input id from inspect")
    parser.add_argument("-b", "--button_value", required=True, help="Button value from inspect")
    parser.add_argument("-l", "--list", required=True, help="Absolute path to the file containing list of xss payload")

    args = parser.parse_args()

    if not os.path.isabs(args.list):
        print("Error: Please provide an absolute path for the file.")

    if not os.path.exists(args.list):
        print(f"Error: File '{args.list}' does not exist.")

    xss.xss(args.url, args.input_id, args.button_value, args.list)


if __name__ == "__main__":
    main()
