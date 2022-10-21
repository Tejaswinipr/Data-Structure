#creating a stack
def create_stack():
    stack=[]
    return stack
    
#checking an empty stack
def isEmpty(stack):
    return len(stack)==0
    
#Adding items into stack
def push(stack,item):
    stack.append(item)
    print(item+"pushed")
    
#Deleting an item from the stack
def pop(stack):
    if isEmpty(stack):
        return "Stack is Empty"
        
    return stack.pop()
    
stack=create_stack()
push(stack,str(5))
push(stack,"jkkl")
push(stack,"89")
push(stack,"lfhj")
print(stack)
print(pop(stack))
print((stack))
    
