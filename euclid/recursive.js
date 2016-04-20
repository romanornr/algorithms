//n is the largest number
var GCD = function (m, n){
	if((m % n) == 0){
		return n;
	}
		return GCD(n, m %n)
}

GCD(21, 35);d
