from dataclasses import dataclass

if __name__=="__main__":
  print("only meant to be an include, don't run directly")

# This is a file that defines what a printjob is.
@dataclass
class PrintJob:
  fileName: str
  personName: str
  approverName: str
  printerID: int
  classPeriod: str
  boxToBePlacedIn: str = ""
  def setBox(self, box: str):
    self.boxToBePlacedIn = box