describe("test getArrayOfDates function", function () {

    // Testing getArrayOfDates to return undefined
    it("arrayOfDates should be undefined", function () {
        var arrayOfDates = getArrayOfDates();
        expect(arrayOfDates).not.toBeDefined();
    });
});

describe("test clearMap function", function () {

    // Expect markersArray to be an empty list
    it("clearMap should return empty list", function () {
        expect(markersArray).toEqual([]);
    });
});