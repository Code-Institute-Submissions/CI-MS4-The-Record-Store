

Access main [README](https://github.com/Kieran-Murray-Code/CI-MS4-The-Record-Store/blob/master/README.md) file.

### Testing User Stories
#### Shopper
1. As a shopper I want to be able to view all products available to purchase.
	-  Using the navigation bar I can select the Genres dropdown menu and select All to view all products available on the site.
2. As a shopper I want to be able to search, sort and filter products to find a product that I want.
	-	Using the search bar in the main site navigation bar I can search for a product by name, artist, label, description, tracklist(song name)
	-	Using the main site navigation Genre dropdown menu I can select a genre to show only products in that genre.
	-	Using main site navigation Promotions dropdown menu I can select a promotion to show only products in that promotion.
	-	When viewing all products of a certain filter I can sort the results by price (low-high or high to low) or alphabetically (a-z or z-a)
	-	When viewing all products of a certain filter I can further filter my results using the filter panels provided for price range, genre, artist, label, format, colour and tag.
3. As a shopper I want to be able to see individual product details.
	-  When viewing all products of a certain filter I can click on the product name to go a page showing all the products details including a product description, tracklist, format, colour and genre.
4. As a shopper I want add/remove products to/from my cart as well as manage quantities of products in my cart. 
	- When browsing products I can hover over a product and get an overlay with an add to cart button.
	- When view a product details I can click on the add to cart button.
	- When viewing the cart I can adjust the quantity of a product by using the + or - buttons on the quantity input.
	- When viewing the cart I can remove a product from the cart by clicking on the trash can button.
5. As a shopper I want add/remove products to/from a wishlist.
	 - When browsing products I can hover over a product and get an overlay with an add to wishlist button.
	- When view a product details I can click on the add to wishlist button.
	- When viewing the wishlist I can hover over a product and get an overlay with a remove from wishlist button.
	- When viewing the wishlist can click on the remove all button to remove all product from the wishlist at once.
6. As a shopper I want to be able to pay for products with a credit card.
	- On the checkout page there is a stripe payments credit card input that validates credit card payments securely.
7. As a shopper I want to be able to checkout as a guest.
	- An account isn't required to checkout, order can be placed without logging in.
8. As a shopper I want to be able to create a user account to save details for quicker checkouts.
	- During checkout I'm informed that I can sign up to save my details with a link to to the signup page.
	- I can click on the profile icon on the main navbar from any page and I will be taken to the sign in page, on the sign in page there is a link for new customers to sign up.
	- When I have created an account I can add an address to my address book and set it as my primary address, this address will populate the order form on the checkout.
	- During checkout if I'm signed in I can check the save address checkbox to save the address in the order form to my account if it's a new address.
9. As a shopper I want to be able to create a user account to store and view my order history.
	- I can click on the profile icon on the main navbar from any page and I will be taken to the sign in page, on the sign in page there is a link for new customers to sign up.
	- When I have created an account I can click on the profile to be taken to my account page where I can view my order history.
10. As a shopper I want to be able to create a user account to store and recall my wishlist. 
	- I can click on the profile icon on the main navbar from any page and I will be taken to the sign in page, on the sign in page there is a link for new customers to sign up.
	- Whenever I log in to my account, any items in the session wishlist that are not in the wishlist saved to my account will be added to by wishlist and saved. Then my account wishlist will be loaded into the session.
	- When I log in if there is no items in the session wishlist then my account wishlist will be loaded into the session.


#### Store Owner
1.  As a store owner I want to sell my products. 
	 - A payment system using Stripe Payments is integrated in the site and I can accept payments for products from customers.
2. As a store owner I want to be able to add new products to the store. 
	- When signed in as a superuser the admin icon will appear on the navbar beside the cart icon, clicking on this will open up the add product page.
	- On the add product page I can fill in the product details, upload and upload a product image.
	- The add product form uses Select2 to allowing dynamic option creation on the dropdown selects for Artist, Genre, Label, Colour, Format and Tag to allow new options to be added to the database when creating a product with having to add them manually in the admin panel.
 3. As a store owner I want to be able to edit and delete existing products in the store.
	- When signed in as a superuser and on the view products page an edit & delete button will appear below each product. Clicking on the edit button will bring up the edit product page with the form populated with all existing product data.
	- 
### HTML & CSS Validation

#### HTML
The HTML was put through through [https://validator.w3.org/](https://validator.w3.org/).

The following errors were found and fixed.
**Error**: Element  `div` not allowed as child of element  `ul` in this context
**Error**: Duplicate ID
**Error**: Whitespace in ID
**Error** Attribute `name` on element `input`: Must not be empty.
**Error**: Attribute  `min`  not allowed on element  `input`  at this point.
**Error**: Attribute  `max`  not allowed on element  `input`  at this point.
**Error**: Unclosed element  `div`.
**Error**: The value of the  `for`  attribute of the  `label`  element must be the ID of a non-hidden form control.
**Error**: Stray end tag `input`
**Error**: Stray end tag  `div`.
**Error**: Attribute  `placeholder`  not allowed on element  `select`  at this point.


#### CSS
The following errors were found when running were found when running my **CSS** through [https://jigsaw.w3.org/css-validator/validator](https://jigsaw.w3.org/css-validator/validator)

Any issues found were due to the validator not being up to date with current CSS spec.