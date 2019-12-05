function redLedOn()
{
	system("gpio -g mode 15 out");
	system("gpio -g write 15 1"); //red led
}

function yellowLedOn()
{
	system("gpio -g mode 16 out");
	system("gpio -g write 16 1"); //yellow led
}

function greenLedOn()
{
	system("gpio -g mode 18 out");
	system("gpio -g write 18 1"); //green led
}

function whiteLedOn()
{
	system("gpio -g mode 22 out");
	system("gpio -g write 22 1"); //white led
}

function redLedOff()
{
	system("gpio -g write 15 0");
}

function yellowLedOff()
{
	system("gpio -g write 16 0");
}

function greenLedOff()
{
	system("gpio -g write 18 0");
}

function whiteLedOff()
{
	system("gpio -g write 22 0");
}
