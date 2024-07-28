from unittest import TestCase,main
from utils.file_helpers import *

class FileHelpersTest(TestCase):
    def test_get_file_extension(self):
        path1 : str = "./file_name/this.json"
        path2 : str =  "./file_name"
        path3 : str = "this.json"

        self.assertEqual(get_file_extension(path1),"json")
        self.assertEqual(get_file_extension(path2),None)
        self.assertEqual(get_file_extension(path3),"json")

    

if __name__ == "__main__":
    main()