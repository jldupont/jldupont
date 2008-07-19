/**
 * @author Jean-Lou Dupont
 */
package widget_commands;

import org.jldupont.command.Command;
import org.jldupont.command.CommandStatus;

import com.google.gwt.user.client.ui.Widget;

public class ListeUpdaterCommand 
	extends Command 
	implements WidgetCommandInterface {

	final static String thisClass ="org.jldupont.widget_commands.ListeUpdaterCommand";
	
	/**
	 * The parameter name to look for
	 */
	String paramName = null;
	
	/**
	 * Widget
	 */
	Widget w = null;
	
	/*===================================================================
	 * Constructors 
	 ===================================================================*/
	public ListeUpdaterCommand( ) {
		super( thisClass, "default_id", true );
	}
	
	public ListeUpdaterCommand( String id ) {
		super( thisClass, id, true );
	}
	/*===================================================================
	 * WidgetCommandInterface
	 ===================================================================*/
	/**
	 * Setter
	 * @param w
	 */
	public void setWidget(Widget w) {
		this.w = w;
	}
	
	/**
	 * Clears the widget's content
	 */
	public void clearWidget() {
		
	}
	
	/*===================================================================
	 * CommandInterface
	 ===================================================================*/
	
	@Override
	public void setParameterName( String paramName ) {
		this.paramName = paramName;
	}
	
	@Override
	protected CommandStatus _run() {
		
		// retrieve list
		
		// clear widget's view
		
		// update widget
		
		return null;
	}
	
	@Override
	protected void _onError() {
		// TODO Auto-generated method stub
	}

	@Override
	protected void _onPending() {
		// TODO Auto-generated method stub
	}

	@Override
	public void setStatus(CommandStatus s) {
		// TODO Auto-generated method stub

	}

}//endclass
