<?xml version="1.0" encoding="UTF-8" ?>
<f xmlns="http://pear.php.net/dtd/rest.categorypackageinfo"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xsi:schemaLocation="http://pear.php.net/dtd/rest.categorypackageinfo
    http://pear.php.net/dtd/rest.categorypackageinfo.xsd">
<pi>
	<p>
		 <n>$package_name$</n>
		 <c>$channel_name$</c>
		 <ca xlink:href="$category_path$">$category_name$</ca>
		 <l>$license$</l>
		 <s>$summary$</s>
		 <d>$description$</d>
		 <r xlink:href="$releases_path$"/>
	</p>
	<a>
	 <!-- put latest release information here -->
	 <!-- This is the information that appears when doing list-all command -->

		$releases$
		
		<!-- example:
		<r>
			<v>0.1.0</v>
			<s>beta</s>
		</r>
		-->
	</a>
</pi>
</f>