 Fs = 1000; 
 t = linspace(0,1-1/Fs,Fs);
 f = 15;
 a = 4;
 y = a*sin(2*pi*f*t);
 plot(t,y);
 
 