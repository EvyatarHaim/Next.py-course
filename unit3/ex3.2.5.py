def read_file(file_name):
    try:
        print("__CONTENT_START__")
        file = open(file_name)

    except IOError:
        print("__NO_SUCH_FILE__")

    else:
        print(file.readline().strip())
        file.close()

    finally:
        print("__CONTENT_END__")


print(read_file(r"C:\Networks\Sigit\Next\unit3\file.txt"))
print(read_file("file_does_not_exist.txt"))
