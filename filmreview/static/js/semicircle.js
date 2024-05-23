document.addEventListener('DOMContentLoaded', function() {
    var container = document.getElementById('container'); 
    var score = parseFloat(container.getAttribute('score')) / 100;

var bar = new ProgressBar.SemiCircle(container, {
    strokeWidth: 6,
    color: '#FFEA82',
    trailColor: '#eee',
    trailWidth: 1,
    easing: 'easeInOut',
    duration: 1000,
    svgStyle: null,
    text: {
      value: 'Calculating...',
      alignToBottom: false
    },
    from: {color: '#FFEA82'},
    to: {color: '#ED6A5A'},
    // Set default step function for all animate calls
    step: (state, bar) => {
      bar.path.setAttribute('stroke', state.color);
      var value = Math.round(bar.value() * 100);
      if (value === 0) {
        bar.setText('');
      } else {
        bar.setText(value + "%");
      }
      
      if(value > 75){
        bar.text.style.color = 'green';
        bar.path.setAttribute('stroke', 'green');
      }
      else if (value > 60){
        bar.text.style.color = 'orange'
        bar.path.setAttribute('stroke', 'orange');
      }
      else{
        bar.text.style.color = 'red'
        bar.path.setAttribute('stroke', 'red');
      }
    }
  });
  bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
  bar.text.style.fontSize = '2rem';
  
  bar.animate(score);  // Number from 0.0 to 1.0
});