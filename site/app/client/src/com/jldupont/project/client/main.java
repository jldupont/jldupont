/**
 * GWT - www.jldupont.com
 * 
 * @author Jean-Lou Dupont
 */
package com.jldupont.project.client;

import com.google.gwt.user.client.Element;
import com.google.gwt.user.client.DOM;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.WindowResizeListener;
import com.google.gwt.user.client.Command;
import com.google.gwt.user.client.DeferredCommand;
import com.google.gwt.user.client.ui.FlexTable;
import com.google.gwt.user.client.ui.FlowPanel;
import com.google.gwt.user.client.ui.HasHorizontalAlignment;
import com.google.gwt.user.client.ui.Image;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.TextBox;
import com.google.gwt.user.client.ui.TextBoxBase;

import org.jldupont.widget.GoogleGears;
import org.jldupont.widget.ImgAnchorLink;

/**
 * Entry point classes define <code>onModuleLoad()</code>.
 */
public class main implements EntryPoint, WindowResizeListener {
	
	private FlexTable flexTableMain = new FlexTable();
	private ImgAnchorLink ImgLinkedin = new ImgAnchorLink();
	private ImgAnchorLink ImgBlog = new ImgAnchorLink();
	private ImgAnchorLink ImgWiki = new ImgAnchorLink();
	private ImgAnchorLink ImgProjects = new ImgAnchorLink();
	private TextBox TextTitle = new TextBox();
	
	public void onModuleLoad() {
		RootPanel.get();
		RootPanel rootPanel = RootPanel.get();
		rootPanel.setSize("100%", "100%");
		rootPanel.setStylePrimaryName("rootPanel");
		rootPanel.setStyleName("rootPanel");

		rootPanel.add(flexTableMain, 60, 125);
		flexTableMain.setBorderWidth(1);
		flexTableMain.setStyleName("gwt-TabPanel");
		flexTableMain.setSize("377px", "270px");
		flexTableMain.setCellSpacing(5);
		flexTableMain.setCellPadding(5);

		// LinkedIn
		flexTableMain.setWidget(0, 0, ImgLinkedin);
		ImgLinkedin.setStylePrimaryName("gwt-Image");
		flexTableMain.getCellFormatter().setHorizontalAlignment(0, 0, HasHorizontalAlignment.ALIGN_CENTER);
		ImgLinkedin.setTarget("_blank");
		ImgLinkedin.setHref("http://www.linkedin.com/in/JeanLouDupont");
		ImgLinkedin.setId("link_linkedin");
		ImgLinkedin.setImgUrl("linkedin.gif");
		ImgLinkedin.setImgClass("gwt-Image");
		ImgLinkedin.setTitle("my LinkedIn profile");

		// Blog
		flexTableMain.setWidget(0, 1, ImgBlog);
		flexTableMain.getCellFormatter().setHorizontalAlignment(0, 1, HasHorizontalAlignment.ALIGN_CENTER);
		ImgBlog.setStylePrimaryName("gwt-Image");
		ImgBlog.setImgClass("gwt-Image");
		ImgBlog.setTarget("_blank");
		ImgBlog.setHref("http://jldupont.blogspot.com");
		ImgBlog.setId("link_blog");
		ImgBlog.setImgUrl("blog.jpg");
		ImgBlog.setTitle("my WEBlog");		

		// Mediawiki Wiki
		flexTableMain.setWidget(1, 0, ImgWiki);
		ImgWiki.setStylePrimaryName("gwt-Image");
		ImgWiki.setImgClass("gwt-Image");
		flexTableMain.getCellFormatter().setHorizontalAlignment(1, 0, HasHorizontalAlignment.ALIGN_CENTER);
		ImgWiki.setTarget("_blank");
		ImgWiki.setHref("http://wiki.jldupont.com");
		ImgWiki.setId("link_wiki");
		ImgWiki.setImgUrl("wiki.png");
		ImgWiki.setTitle("my Mediawiki site & extensions");

		// Projects
		flexTableMain.setWidget(1, 1, ImgProjects);
		ImgProjects.setStylePrimaryName("gwt-Image");
		ImgProjects.setImgClass("gwt-Image");
		flexTableMain.getCellFormatter().setHorizontalAlignment(1, 1, HasHorizontalAlignment.ALIGN_CENTER);
		ImgProjects.setTarget("_blank");
		ImgProjects.setHref("http://code.google.com/u/JeanLou.Dupont/");
		ImgProjects.setId("link_projects");
		ImgProjects.setImgUrl("projects.jpg");
		ImgProjects.setTitle("my open projects");
		flexTableMain.getCellFormatter().setHorizontalAlignment(1, 0, HasHorizontalAlignment.ALIGN_CENTER);

		final FlowPanel flowPanelHeader = new FlowPanel();
		rootPanel.add(flowPanelHeader, 0, 0);
		flowPanelHeader.setSize("100%", "5%");

		// HEADER
		final FlexTable flexTableHeader = new FlexTable();
		flowPanelHeader.add(flexTableHeader);
		flexTableHeader.setSize("100%", "100%");

		final Image image = new Image();
		flexTableHeader.setWidget(0, 0, image);
		flexTableHeader.getCellFormatter().setWidth(0, 0, "116px");
		image.setUrl("bluecortex2.gif");

		// HEADER - Title
		TextTitle.setStyleName("title");
		flexTableHeader.setWidget(0, 1, TextTitle);
		TextTitle.setTextAlignment(TextBoxBase.ALIGN_LEFT);
		TextTitle.setTitle("title");
		TextTitle.setText("Jean-Lou Dupont's WEB site");
		TextTitle.setWidth("100%");

		// FOOTER
		// ===============================================
		final FlowPanel flowPanelFooter = new FlowPanel();
		rootPanel.add(flowPanelFooter, 0, 419);
		flowPanelFooter.setSize("100%", "5%");

		final FlexTable flexTableFooter = new FlexTable();
		flowPanelFooter.add(flexTableFooter);
		flexTableFooter.setSize("100%", "100%");
		flexTableFooter.getCellFormatter().setHorizontalAlignment(0, 1, HasHorizontalAlignment.ALIGN_RIGHT);

		final FlowPanel flowPanelContentFooter = new FlowPanel();
		flexTableFooter.setWidget(0, 1, flowPanelContentFooter);

		final Image ImgGwt = new Image();
		flowPanelContentFooter.add(ImgGwt);
		ImgGwt.setUrl("gwt.png");
		ImgGwt.setTitle("built using GoogleWebToolkit + GWT Designer");

		final Image ImgGae = new Image();
		flowPanelContentFooter.add(ImgGae);
		ImgGae.setUrl("gae.png");
		ImgGae.setTitle("built using GoogleAppEngine");

		final GoogleGears googleGears = new GoogleGears();
		flowPanelContentFooter.add(googleGears);
		//flexTableFooter.getCellFormatter().setWidth(0, 1, "49px");

		// EMAIL
		final ImgAnchorLink imgAnchorLink = new ImgAnchorLink();
		flexTableFooter.setWidget(0, 0, imgAnchorLink);
		flexTableFooter.getCellFormatter().setWidth(0, 0, "152px");
		imgAnchorLink.setHref("mailto:jld@jldupont.com");
		imgAnchorLink.setImgUrl("mailto.png");
		imgAnchorLink.setTitle("mailto:jld@jldupont.com");
		imgAnchorLink.setStylePrimaryName("gwt-Image");
		
	    DeferredCommand.addCommand(new Command() {
	        public void execute() {
	          onWindowResized(Window.getClientWidth(), Window.getClientHeight());
	        }
	      });

	    onWindowResized(Window.getClientWidth(), Window.getClientHeight());
		
	    Window.addWindowResizeListener(this);
	    
	}
		/*TODO
		 * (non-Javadoc)
		 * @see com.google.gwt.user.client.WindowResizeListener#onWindowResized(int, int)
		 */
	public void onWindowResized(int width, int height) {
		
		Element ft = flexTableMain.getElement();
		
		int ww = this.flexTableMain.getOffsetWidth();
		
		int l = (width - ww) / 2;

		DOM.setStyleAttribute(ft, "position", "absolute");
		DOM.setStyleAttribute(ft, "left", l + "px");	
	}

}
