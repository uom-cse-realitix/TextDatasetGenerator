from string import Template

def generate_operation(template_operations, operation_type, objects=None, no_op=False):
    '''
    Generates operation texts from templates and returns list.

    :param template_operations: List of template operations
    :param objects: Object names that need to be inserted
    :param operation_type: Class of operation
    :return: List of generated operations for operation type
    '''

    generated_op = ''
    generated_ops = []
    for op in template_operations:
        #Adding operation placeholder at the end of operate template
        op = op + ', $operation' + '\n'
        s = Template(op)

        if not no_op and objects:
             for obj in objects:
                #Replacing placeholders
                generated_op = s.substitute(object=obj, operation=operation_type)
                # print(generated_op)
                generated_ops.append(generated_op)
        else:
            generated_op = s.substitute(operation=operation_type)
            generated_ops.append(generated_op)            
    return generated_ops


OBJECTS = ['laptop',
           'book',
           'cup',
           'mobile phone',
           'pen',
           'bottle',
           'hand',
           'chair',
           'mouse',
           'monitor',
           'keyboard']

locate_operations = ('Find the $object',
                     'Show me the location of $object',
                     'Locate the $object',
                     'Please locate the $object',
                     'Where is the $object',
                     'Where are the ${object}s',
                     'What is the location of $object',
                     'What are the locations of ${object}s',
                     'Can you find the $object for me?',
                     'Point out the $object',
                     'Detect $object',
                     'Spot the $object',
                     'Highlight the $object',
                     'Color the $object',
                     'Show me where the $object is',
                     'Show me where the $object are',
                     'Detect the $object',
                     'Search for the $object',
                     'Find where the $object is',
                     'Find where the $object are',
                     'Discover the $object',
                     'Track the $object',
                     'Point me the $object',
                     'Where did I put my $object',
                     'Where did I keep my $object',
                     'I need to find my $object',
                     'Can you help find my $object',
                     'Help me find my $object',
                     'Is there a $object here',
                     'I can’t find my $object')

describe_operations = ('Give me information about the $object',
                       'Show me the properties of $object',
                       'Describe $object',
                       'Give me the details about $object',
                       'Make me aware of $object',
                       'Show properties of this $object',
                       'What are the features of the $object',
                       'What are the properties of the $object',
                       'Give a detailed description of $object',
                       'Give an account of this $object',
                       'Explain the features of this $object',
                       'Explain the properties of this $object',
                       'What is the brand of the $object',
                       'Who is the manufacturer of $object',
                       'What kind of $object is this?',
                       'I want the details of this $object',
                       'Search the details of this $object',
                       'Provide the details of this $object',
                       'Can I know more about the  $object',
                       'Can I get information about the $object',
                       'What can you say about this $object',
                       'What do you know about the $object',
                       'What is this $object',
                       'Give me the specification of the $object',
                       'Can you describe this $object')

no_Op_lines = []

for line in open('/home/ashen/Documents/GitHubRepos/pykaldi/examples/setups/zamia/out/test/decode.out', 'r'):
    if line.strip():
        no_Op_lines.append(line.rstrip('\n'))

dataset_text_file = open(r'/home/ashen/Documents/Dataset_text_classification.txt', 'w+')

dataset_text_file.writelines(generate_operation(locate_operations, '1', objects=OBJECTS))
dataset_text_file.writelines(generate_operation(describe_operations, '2', objects=OBJECTS))
dataset_text_file.writelines(generate_operation(no_Op_lines, '3', no_op=True))

dataset_text_file.close()