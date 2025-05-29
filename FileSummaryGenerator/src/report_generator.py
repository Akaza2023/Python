class ReportGenerator:
    def __init__(self):
        self.__lines = [] # here __lines is private attribute

    def add_line(self, line: str):
        """Adding a line to the internal report"""
        self.__lines.append(line)

    def save(self, filepath: str):
        """Writes the report buffer to a file"""
        with open(filepath, 'w') as f:
            for line in self.__lines:
                f.write(line + '\n')