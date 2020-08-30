window.onscroll=function(){
	var menu = document.getElementById("menu");
	 var winScroll = document.documentElement.scrollTop || document.body.scrollTop;
	 var flag =0;
	 if(winScroll>20 && flag === 0){ 
	 	flag = 1;
	 	menu.style.animation="mymove 1s ease-in";
	 	menu.style.animationFillMode = "forwards";
	 }else{
	 	flag = 0;
		menu.style.animation="mymove1 1s ease-out";
		menu.style.animationFillMode = "forwards";
	 }
}