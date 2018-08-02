(function($){
 	$.fn.extend({  		
	    //pass the options variable to the function
		percentcircle: function(options) {
		//Set the default values, use comma to separate the settings, example:

		
							
							



			var that = this,
			template = '<div><div class="ab"><div class="cir"><span class="perc">{{percentage}}</span></div></div></div>',
			defaults = {
			        animate : true,
					diameter : 150,
					guage: 2,
					coverBg: '#fff',
					bgColor: '#efefef',
					fillColor: '#5c93c8',
					percentSize: '15px',
					percentWeight: 'normal'
				},
				options =  $.extend(defaults, options),
				styles = {
				    cirContainer : {
					    'width':options.diameter,
						'height':options.diameter
					},
					cir : {
					    'position': 'relative',
					    'text-align': 'center',
					    'width': options.diameter,
					    'height': options.diameter,
					    'border-radius': '100%',
					    'background-color': options.bgColor,
					    'background-image' : 'linear-gradient(91deg, transparent 50%, '+options.bgColor+' 50%), linear-gradient(90deg, '+options.bgColor+' 50%, transparent 50%)'
					},
					cirCover: {
						'position': 'relative',
					    'top': options.guage,
					    'left': options.guage,
					    'text-align': 'center',
					    'width': options.diameter - (options.guage * 2),
					    'height': options.diameter - (options.guage * 2),
					    'border-radius': '100%',
					    'background-color': options.coverBg
					},
					percent: {
						'display':'block',
						'width': options.diameter,
					    'height': options.diameter,
					    'line-height': options.diameter + 'px',
					    'vertical-align': 'middle',
					    'font-size': options.percentSize,
					    'font-weight': options.percentWeight,
					    'color': options.fillColor
                    }
				};
			

			function init(){
				that.each(function(){
					var $this = $(this),
					    //we need to check for a percent otherwise set to 0;
						perc = Math.round($this.data('percent')), //get the percentage from the element
						text = ($this.data('text')),
						deg = perc * 3.6,
						stop = options.animate ? 0 : deg,
						// $chart = $(template.replace('{{percentage}}',perc+'%'));
						$chart = $(template.replace('{{percentage}}',text));
						//set all of the css properties forthe chart
						$chart.css(styles.cirContainer).find('.ab').css(styles.cir).find('.cir').css(styles.cirCover).find('.perc').css(styles.percent);
					
					$this.append($chart); //add the chart back to the target element
					setTimeout(function(){
						animateChart(deg,parseInt(stop),$chart.find('.ab')); //both values set to the same value to keep the function from looping and animating	
					},250)
	   	    	});
			}

			var animateChart = function (stop,curr,$elm){
				var deg = curr;
				if(curr <= stop){
					if (deg>=180){
						$elm.css('background-image','linear-gradient(' + (90+deg) + 'deg, transparent 50%, '+options.fillColor+' 50%),linear-gradient(90deg, '+options.fillColor+' 50%, transparent 50%)');
			  	    }else{
			  		    $elm.css('background-image','linear-gradient(' + (deg-90) + 'deg, transparent 50%, '+options.bgColor+' 50%),linear-gradient(90deg, '+options.fillColor+' 50%, transparent 50%)');
			  	    }
					curr ++;
					setTimeout(function(){
						animateChart(stop,curr,$elm);
					},1);
				}
			};			
			
			init(); //kick off the goodness
   	    }
	});
	
})(jQuery);