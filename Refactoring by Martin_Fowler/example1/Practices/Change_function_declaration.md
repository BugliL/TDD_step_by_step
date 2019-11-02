# Change function declaration
Consist in modifying the function signature, parameters and or function
name.

## How to change function declaration
The signature change can be made directly if it's simple to do
or can be made in small steps

### Simple - Direct
 * To eliminate a parameter check out if there are references to
 that parameter
 * Change function signature
 * Update all function call

### Migration - In small steps
 * Refactor the function
 * Use "Extract function" on the function body to create a new function
 * Add all needed parameters
 * Apply "Inline function" to the old function
