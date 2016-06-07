int addDigits(int num) {
    if ( num == 0 ) {
        return 0;
    }

    int remainder = num % 9;    
    if ( remainder == 0 ) {
        remainder = 9;
    }

    return remainder;
}

int main() {

    return 0;
}
