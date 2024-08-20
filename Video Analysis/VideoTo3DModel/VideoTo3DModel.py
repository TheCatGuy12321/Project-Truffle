import sys, modeler, os
if len(sys.argv) < 3:
    print("Usage: python %s (input video path) (sample rate)"%sys.argv[0])
    exit(0)

output_path = r"C:\Users\love_\jay\Coding\GitProjects\Project-Truffle\Video Analysis\VideoTo3DModel\outputs"
input_path = sys.argv[1]
sample_rate = int(sys.argv[2])

if "-o" in sys.argv and len(sys.argv) == 5:
    output_path = sys.argv[4]

os.system("cd outputs")
sfm = modeler.SfM(output_path, False, input_path, sample_rate)
sfm.find_structure_from_motion()
os.system("rm -r input_images")