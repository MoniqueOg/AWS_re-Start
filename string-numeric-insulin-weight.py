#Store the human preproinsulin sequence in a variable called preproinsulin:

preproInsulin ="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:

lsInsulin= "malwmrllpllallalwgpdpaaa"

bInsulin= "fvnqhlcgshlvealylvcgergffytpkt"

aInsulin= "giveqcctsicslyqlenycn"

cInsulin= "rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin

# Printing "the sequence of human insulin" to console using successive print() commands:

print("The sequence of human preproinsulin:")

print(preproInsulin)

# Printing to console using concatenated strings inside the print function (one-liner):

print("The sequence of human insulin, chain a: " + aInsulin)

#The built-in print() function accepts multiple arguments that can accomplish the same task in step 5. For example:
#print("The sequence of human insulin, chain a:", aInsulin)
