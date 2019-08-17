import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)

# If we didn't want to empty the list of unprinted designs, we could do this:
# print_models(unprinted_designs[:], completed_models)
# The slice notation here makes a copy of the list to send to the function.
# The original list will be unaffected.
# Only keep a copy when needed - in most cases, the original list should be used.

printing_functions.show_completed_models(completed_models)
