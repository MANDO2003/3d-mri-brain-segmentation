describe("Main Util Functions", function () {

  describe('#labelMax()', function () {
    it('return max', function () {
       expect( labelMax( [1,2,3]) ).to.equal(3);
    });
  });

  describe('#arrValuesFreq()', function () {
    it('return frequence of  array unique values', function () {
       expect( arrValuesFreq( [2, 2, 2, 2, 3]) ).to.be.a('map');
    });
  });  

  describe('#map2Object()', function () {
    it('convert map to  JSON object, and it needs JS ES6', function () {
       expect( map2Object(  new Map().set('a', 1).set('b', 2) ) ).to.eql({ a: 1, b: 2 });
    });
  });   

});  