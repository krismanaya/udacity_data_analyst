// d3 practice for udacity

// create svg and insert into DOM 
var svg = d3.select('.main').append('svg'); 

// make svg element larger in the DOM 
svg.attr('width', 600).attr('height', 300); 

//make linear scale lowest value in years --> highest pixles.  
var y = d3.scale.linear().domain([15,90]).range([250, 0]);
// y(15) --> 250, y(90) --> 90 

//make linear scaled lowest value value in dollars --> highest pixels. 
var x = d3.scale.log().domain([250, 100000]).range([0, 600]);

// making r scaling circles. 
var r = d3.scale.sqrt().domain([52070, 1380000000]).range([10, 40]);

// let's make sure this works
console.log(y(77), x(13330), r(1380000000)); 

// make the circle 
svg.append('circle').attr('fill','red')
                    .attr('r',r(1380000000))
                    .attr('cx',x(13330))
                    .attr('cy',y(77)); 

