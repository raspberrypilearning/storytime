## If, Elif, and Else

Having discovered the gender of the user, you can use that information in your story. But as you know from your literacy lessons, nouns are preceded with 'he and 'she' and not 'girl' or 'boy', which are the values currently stored in the `gender` variable. You can fix this by using a computing concept to help out here; it's called a **conditional**.

- Underneath the `input` and `print` statements type:

	```python
	if gender == "girl":
	    pronoun = "she"
	```
	These two lines of code state that *if* the answer to the question 'Are you a girl or boy?' is 'girl', then set the pronoun to be 'she'. This is a condition. 
		
2. Now you need to set the pronoun if the answer to the question is 'boy':
	
	```python
	elif gender == "boy":
	    pronoun = "he"
	```
	`elif` means 'else, if'. 
	
3. But what if the user doesn't type 'girl' or 'boy'? Well, you can cover this situation by typing:	
	```python        
	else:
	    pronoun = "it"
	```    
4. Save your work so far by clicking on **File** and **Save**.
	
	
	![](images/story3.png)

