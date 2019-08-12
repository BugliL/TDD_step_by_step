package tests;

// using Junit5.4

import model.Dollar;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

//
//  Todo:
//     $5 + 10 CHF = $10 if CHF:USD is 2:1
//     $5 * 2 = $10
//     Dollar side-effects?
//     Money rounding?

public class DollarTest {

    @Test
    public void given_5_Dollar_when_multiplied_by_3_and_2_than_result_15() {
        Dollar five = new Dollar(5);
        Dollar ten = five.times(2);
        assertEquals(10, ten.amount);
        Dollar fifthteen = five.times(3);
        assertEquals(15, fifthteen.amount);
    }
}
