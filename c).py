class MPNeuron:
    def __init__(self,n=3,inputs=[1,1,1],weights=[1,1,1],thresh=2.5):
        self.n=n
        self.inputs=inputs
        self.weights=weights
        self.thresh=thresh
    def MP_Neuron_Input(self):
        self.inputs=[]
        self.weights=[]
        self.n=int(input("Enter no. of inputs"))
        for i in range(0,self.n):
            a=int(input("enter input values one by one"))
            self.inputs.append(a)
        for i in range(0,self.n):
            b=int(input("enter weights one by one with -1 inhibitory and +1 excitatory"))
            self.weights.append(b)
        self.thresh=float(input("Enter theta"))
    def MP_Neuron_Evaluate(self):
        result=0
        for i in range(0,self.n):
           result=result+self.inputs[i]*self.weights[i]
        final=result+self.thresh
        if final >= 0:
            return 1
        elif final <0:
            return 0
nand=MPNeuron()
nand.MP_Neuron_Input()
res=nand.MP_Neuron_Evaluate()
print(res)
        
            
        
        
    
            
    
            
            
            
        
        
        
