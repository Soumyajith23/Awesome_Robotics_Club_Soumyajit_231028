PART A and PART b is done with the given algorithm in FABRIK documentation
• Given:	joint	positions	pi for	i =	1	to	n,	the	target	position	t and	the	
distances	between	each	joint	di =	|pi+1-pi
|	for	i	=	1,.	.	.,n-1
• if	|p1-t| >	d1 +	d2 +.	.	.+	dn-1 then //	 target	is	unreachable
find	the	vector	(t-p1)	and	find	the	relative	position	of	each	point	along	that	vector.	i.e.	
imagine	stretching	out	the	complete	chain	in	target’s	direction.
• else //	 target	is	reachable
• Set	b=p1	as	the	initial	 (root)	position
• Find	distance	 of	end-effector	 from	target	i.e.	diff	=	|pn-t|
• While	 (diff	>	tolerance)
• Perform	forward	and	backward	pass


Forward	and	Backward	pass
• Move	the	end-effector	to	t,	i.e.	pn =	t
• For	each	of	the	previous	point	pi
,	i =	n-1	to	1:
find	the	vector	(pi+1 – pi
),	and	the	new	position,	 pi as	 the	relative	position	 of	that	
joint	along	this	vector.
• Now,	our	root	pi would	be	somewhat	shifted	from	its	initial	position	b,	
set	p1 =	b
• For	each	of	the	next	point	pi
,	i =	1	to	n-1:
Find	 the	vector	(pi – pi+1),	 and	 the	new	 position,	 pi+1’	 as	the	relative	position	 of	 that	joint	 along	 this	 vector.
• Update	 the	new	diff	=	|pn-t|
