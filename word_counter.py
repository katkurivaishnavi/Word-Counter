def count_words(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            print(f"Total number of words: {len(words)}")

    except FileNotFoundError:
        print(" File not found. Please check the file name.")

    except Exception as e:
        print(" An error occurred:", e)


# Main execution
file_name = input("Enter the file name: ")
count_words(file_name)
