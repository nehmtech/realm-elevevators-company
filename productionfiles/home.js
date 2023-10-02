/*javascript for sticky menu*/

$(window).scroll(function(){
    if(this.scrollY > 20){
        $('.navbar').addClass("sticky");
    }
    else{
        $('.navbar').removeClass("sticky");
    }
});

        // Typed animation
        var type = new Typed(".typing",{
            strings: ["Transform your business with cutting-edge IT solutions", "Accelerate your success with our expert IT services", "Experience the power of technology-driven growth"],
            typeSpeed: 30,
            backSpeed: 10,
            loop: true,
        });


        /*code for counter up*/
    // Create an array of objects with id and maxCount values
    const counters = [
        { id: 'counter1', maxCount: 100,},
        { id: 'counter2', maxCount: 50 },
        { id: 'counter3', maxCount: 200 },
        { id: 'counter4', maxCount: 30 }
      ];
  
      // Set the interval at which the counters should increase (in milliseconds)
      const interval = 100;
  
      // Loop through each object in the counters array
      counters.forEach(function(counter) {
        // Set the starting point of the counter
        let count = 0;
  
        // Select the element where you want to display the counter
        const counterElement = document.getElementById(counter.id);
  
        // Create the function that increments the counter
        function incrementCounter() {
          // Check if the counter has reached the maximum number
          if (count >= counter.maxCount) {
            // If it has, reset the counter to 0
            count = 0;
          } else {
            // If it hasn't, increment the counter by 1
            count++;
          }
  
          // Display the updated counter value in the selected element
          counterElement.innerHTML = count;
        }
  
        // Call the incrementCounter function every set interval using setInterval()
        setInterval(incrementCounter, interval);
      });
  