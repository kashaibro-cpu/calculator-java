>Ovdje su rezultati testiranja kalkulatora:
>Test slučajUlaz		Očekivani rezultat	Stvarni rezultat	Status	Zapažanje
>1		    2+3	        5			        5			        PASS	Osnovno sabiranje radi ispravno.
>2		    10-4		6			        6			        PASS	Oduzimanje radi ispravno.
>3		    5*4		    20			        20			        PASS	Množenje radi ispravno.
>4		    20/5		4			        4			        PASS	Dijeljenje radi ispravno.
>5		    2+3*4		14                  14			        PASS	Poštuje prioritet množenja.
>6		    10+5*4+3	33			        33			        PASS 	Složeni izraz se računa ispravno.
>7		    -5+2	    -3			        -3			        PASS	Podržani negativni brojevi na početku izraza.
>8		    +5+2		7			        7			        PASS	Podržan znak + na početku izraza.
>9		    10/0		Greška ili Infinity	Infinity		    FAIL	Nema obrade dijeljenja nulom.
>10		    abc		    ERROR			    ERROR			    PASS	Neispravan unos se prepoznaje.
>11		    5++2		ERROR			    ERROR			    PASS	Neispravan izraz se prepoznaje.
>12		    (2+3)*4		20			        ERROR			    FAIL	Kalkulator ne podržava zagrade.



>Uočeni nedostaci:
>-Nije implementirana podrška za zagrade.
>-Dijeljenje nulom vraća Infinity umjesto korisnički razumljive poruke o grešci.
>-Ne postoje validacije za sve vrste neispravnih izraza.
>-Korisnik ne dobija detaljno objašnjenje greške, već samo poruku "ERROR".
>-Mogući problemi sa veoma dugim izrazima zbog rekurzivne implementacije metode Calculate.


import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class CalculatorTest {

    @Test
    public void testCalculateExpression() {
        String result = Calculator.Run("2+3*4"); 
        assertEquals("14.0", result);
    }
}

> **Napomena:** Metoda `Calculate` je privatna (`private`), pa je testirana putem metode `Run()`.