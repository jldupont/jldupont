/**
 * LoginLogout widget
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.widget;

public class LoginLogout 
	extends ImgAnchorLink {

	// Image URLs
	final static String img_login    = "login.gif";
	final static String img_logout   = "logout.gif";
	
	// Tooltips
	final static String title_login  = "Login"; 
	final static String title_logout = "Logout";
	
	String href_login = null;
	String href_logout = null;
	
	public LoginLogout() {
		super();
	}

	public void setLoginHref(String url) {
		this.href_login = url;
	}
	public void setLogoutHref(String url) {
		this.href_logout = url;
	}
	public void setState(String state) {
		if (state=="login") {
			this.setImgUrl(img_login);
			this.setTitle(title_login);
			this.setHref(this.href_login);
		} else {
			this.setImgUrl(img_logout);
			this.setTitle(title_logout);
			this.setHref(this.href_logout);			
		}
	}
		
}//end
