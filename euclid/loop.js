//n2 is the biggest number
n1 = 21;

n2 = 35;

while(n2 > 0){
	reminder = n1 % n2;
	n1 = n2;
	n2 = reminder;
}

console.log(n1);
