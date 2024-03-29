<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @subpackage api
 * @version $Id$
 */
//<source lang=php> 

/**
 * This abstract class implements many basic API functions, and is the base of all API classes.
 * @addtogroup API
 */
abstract class api_base 
{
	// These constants allow modules to specify exactly how to treat incomming parameters.

	const PARAM_DFLT = 0;
	const PARAM_ISMULTI = 1;
	const PARAM_TYPE = 2;
	const PARAM_MAX = 3;
	const PARAM_MAX2 = 4;
	const PARAM_MIN = 5;

	private $mMainModule, $mModuleName, $mModulePrefix;

	/**
	* Constructor
	*/
	public function __construct($mainModule, $moduleName, $modulePrefix = '') {
		$this->mMainModule = $mainModule;
		$this->mModuleName = $moduleName;
		$this->mModulePrefix = $modulePrefix;
	}

	/**
	 * Executes this module
	 */
	public abstract function execute();

	/**
	 * Get the name of the module being executed by this instance 
	 */
	public function getModuleName() 
	{
		return $this->mModuleName;
	}

	/**
	 * Get parameter prefix (usually two letters or an empty string). 
	 */
	public function getModulePrefix() 
	{
		return $this->mModulePrefix;
	}	

	/**
	 * Get the name of the module as shown in the profiler log 
	 */
	public function getModuleProfileName() 
	{
		return 'API:' . $this->mModuleName;
	}

	/**
	 * Get main module
	 */
	public function getMain() 
	{
		return $this->mMainModule;
	}

	/**
	 * If this module's $this is the same as $this->mMainModule, its the root, otherwise no
	 */
	public function isMain() 
	{
		return $this === $this->mMainModule;
	}

	/**
	 * Get result object
	 */
	public function getResult() 
	{
		// Main module has getResult() method overriden
		// Safety - avoid infinite loop:
		if ($this->isMain())
			self :: dieDebug(__METHOD__, 'base method was called on main module. ');
		return $this->getMain()->getResult();
	}

	/**
	 * Get the result data array
	 */
	public function & getResultData() 
	{
		return $this->getResult()->getData();
	}

	/**
	 * Set warning section for this module. Users should monitor this section to notice any changes in API.
	 */
	public function setWarning($warning) 
	{
		$msg = array();
		api_result :: setContent($msg, $warning);
		$this->getResult()->addValue('warnings', $this->getModuleName(), $msg);
	}

	/**
	 * If the module may only be used with a certain format module,
	 * it should override this method to return an instance of that formatter.
	 * A value of null means the default format will be used.  
	 */
	public function getCustomPrinter() 
	{
		return null;
	}

	/**
	 * Generates help message for this module, or false if there is no description
	 */
	public function makeHelpMsg() 
	{
		static $lnPrfx = "\n  ";

		$msg = $this->getDescription();

		if ($msg !== false) {

			if (!is_array($msg))
				$msg = array (
					$msg
				);
			$msg = $lnPrfx . implode($lnPrfx, $msg) . "\n";

			// Parameters
			$paramsMsg = $this->makeHelpMsgParameters();
			if ($paramsMsg !== false) {
				$msg .= "Parameters:\n$paramsMsg";
			}

			// Examples
			$examples = $this->getExamples();
			if ($examples !== false) {
				if (!is_array($examples))
					$examples = array (
						$examples
					);
				$msg .= 'Example' . (count($examples) > 1 ? 's' : '') . ":\n  ";
				$msg .= implode($lnPrfx, $examples) . "\n";
			}

			if ($this->getMain()->getShowVersions()) {
				$versions = $this->getVersion();
				$pattern = '(\$.*) ([0-9a-z_]+\.php) (.*\$)';
				$replacement = '\\0' . "\n    " . 'http://svn.wikimedia.org/viewvc/mediawiki/trunk/phase3/includes/api/\\2';
				
				if (is_array($versions)) {
					foreach ($versions as &$v)
						$v = eregi_replace($pattern, $replacement, $v);
					$versions = implode("\n  ", $versions);
				}
				else
					$versions = eregi_replace($pattern, $replacement, $versions);

				$msg .= "Version:\n  $versions\n";
			}
		}

		return $msg;
	}

	public function makeHelpMsgParameters() 
	{
		$params = $this->getAllowedParams();
		if ($params !== false) {

			$paramsDescription = $this->getParamDescription();
			$msg = '';
			$paramPrefix = "\n" . str_repeat(' ', 19);
			foreach ($params as $paramName => $paramSettings) {
				$desc = isset ($paramsDescription[$paramName]) ? $paramsDescription[$paramName] : '';
				if (is_array($desc))
					$desc = implode($paramPrefix, $desc);

				@ $type = $paramSettings[self :: PARAM_TYPE];
				if (isset ($type)) {
					if (isset ($paramSettings[self :: PARAM_ISMULTI]))
						$prompt = 'Values (separate with \'|\'): ';
					else
						$prompt = 'One value: ';

					if (is_array($type)) {
						$choices = array();
						$nothingPrompt = false;
						foreach ($type as $t)
							if ($t=='')
								$nothingPrompt = 'Can be empty, or ';
							else
								$choices[] =  $t;
						$desc .= $paramPrefix . $nothingPrompt . $prompt . implode(', ', $choices);
					} else {
						switch ($type) {
							case 'namespace':
								// Special handling because namespaces are type-limited, yet they are not given
								$desc .= $paramPrefix . $prompt . implode(', ', self :: getValidNamespaces());
								break;
							case 'limit':
								$desc .= $paramPrefix . "No more than {$paramSettings[self :: PARAM_MAX]} ({$paramSettings[self :: PARAM_MAX2]} for bots) allowed.";
								break;
							case 'integer':
								$hasMin = isset($paramSettings[self :: PARAM_MIN]);
								$hasMax = isset($paramSettings[self :: PARAM_MAX]);
								if ($hasMin || $hasMax) {
									if (!$hasMax)
										$intRangeStr = "The value must be no less than {$paramSettings[self :: PARAM_MIN]}";
									elseif (!$hasMin)
										$intRangeStr = "The value must be no more than {$paramSettings[self :: PARAM_MAX]}";
									else
										$intRangeStr = "The value must be between {$paramSettings[self :: PARAM_MIN]} and {$paramSettings[self :: PARAM_MAX]}";
										
									$desc .= $paramPrefix . $intRangeStr;
								}
								break;
						}
					}
				}

				$default = is_array($paramSettings) ? (isset ($paramSettings[self :: PARAM_DFLT]) ? $paramSettings[self :: PARAM_DFLT] : null) : $paramSettings;
				if (!is_null($default) && $default !== false)
					$desc .= $paramPrefix . "Default: $default";

				$msg .= sprintf("  %-14s - %s\n", $this->encodeParamName($paramName), $desc);
			}
			return $msg;

		} else
			return false;
	}

	/**
	 * Returns the description string for this module
	 */
	protected function getDescription() 
	{
		return false;
	}

	/**
	 * Returns usage examples for this module. Return null if no examples are available.
	 */
	protected function getExamples() 
	{
		return false;
	}

	/**
	 * Returns an array of allowed parameters (keys) => default value for that parameter
	 */
	protected function getAllowedParams() 
	{
		return false;
	}

	/**
	 * Returns the description string for the given parameter.
	 */
	protected function getParamDescription() 
	{
		return false;
	}

	/**
	 * This method mangles parameter name based on the prefix supplied to the constructor.
	 * Override this method to change parameter name during runtime 
	 */
	public function encodeParamName($paramName) 
	{
		return $this->mModulePrefix . $paramName;
	}

	/**
	* Using getAllowedParams(), makes an array of the values provided by the user,
	* with key being the name of the variable, and value - validated value from user or default.
	* This method can be used to generate local variables using extract().
	*/
	public function extractRequestParams() 
	{
		$params = $this->getAllowedParams();
		$results = array ();

		foreach ($params as $paramName => $paramSettings)
			$results[$paramName] = $this->getParameterFromSettings($paramName, $paramSettings);

		return $results;
	}

	/**
	 * Get a value for the given parameter 
	 */
	protected function getParameter($paramName) 
	{
		$params = $this->getAllowedParams();
		$paramSettings = $params[$paramName];
		return $this->getParameterFromSettings($paramName, $paramSettings);
	}

	public static function getValidNamespaces() 
	{
		static $mValidNamespaces = null;
		if (is_null($mValidNamespaces)) {

			global $wgContLang;
			$mValidNamespaces = array ();
			foreach (array_keys($wgContLang->getNamespaces()) as $ns) {
				if ($ns >= 0)
					$mValidNamespaces[] = $ns;
			}
		}
		return $mValidNamespaces;
	}

	/**
	 * Using the settings determine the value for the given parameter
	 * @param $paramName String: parameter name
	 * @param $paramSettings Mixed: default value or an array of settings using PARAM_* constants.
	 */
	protected function getParameterFromSettings($paramName, $paramSettings) 
	{

		// Some classes may decide to change parameter names
		$encParamName = $this->encodeParamName($paramName);

		if (!is_array($paramSettings)) {
			$default = $paramSettings;
			$multi = false;
			$type = gettype($paramSettings);
		} else {
			$default = isset ($paramSettings[self :: PARAM_DFLT]) ? $paramSettings[self :: PARAM_DFLT] : null;
			$multi = isset ($paramSettings[self :: PARAM_ISMULTI]) ? $paramSettings[self :: PARAM_ISMULTI] : false;
			$type = isset ($paramSettings[self :: PARAM_TYPE]) ? $paramSettings[self :: PARAM_TYPE] : null;

			// When type is not given, and no choices, the type is the same as $default
			if (!isset ($type)) {
				if (isset ($default))
					$type = gettype($default);
				else
					$type = 'NULL'; // allow everything
			}
		}

		if ($type == 'boolean') {
			if (isset ($default) && $default !== false) {
				// Having a default value of anything other than 'false' is pointless
				self :: dieDebug(__METHOD__, "Boolean param $encParamName's default is set to '$default'");
			}

			$value = $this->getMain()->getRequest()->getCheck($encParamName);
		} else {
			$value = $this->getMain()->getRequest()->getVal($encParamName, $default);

			if (isset ($value) && $type == 'namespace')
				$type = self :: getValidNamespaces();
		}

		if (isset ($value) && ($multi || is_array($type)))
			$value = $this->parseMultiValue($encParamName, $value, $multi, is_array($type) ? $type : null);

		// More validation only when choices were not given
		// choices were validated in parseMultiValue()
		if (isset ($value)) {
			if (!is_array($type)) {
				switch ($type) {
					case 'NULL' : // nothing to do
						break;
					case 'string' : // nothing to do
						break;
					case 'integer' : // Force everything using intval() and optionally validate limits

						$value = is_array($value) ? array_map('intval', $value) : intval($value);
						$min = isset ($paramSettings[self :: PARAM_MIN]) ? $paramSettings[self :: PARAM_MIN] : null;
						$max = isset ($paramSettings[self :: PARAM_MAX]) ? $paramSettings[self :: PARAM_MAX] : null;
						
						if (!is_null($min) || !is_null($max)) {
							$values = is_array($value) ? $value : array($value);
							foreach ($values as $v) {
								$this->validateLimit($paramName, $v, $min, $max);
							}
						}
						break;
					case 'limit' :
						if (!isset ($paramSettings[self :: PARAM_MAX]) || !isset ($paramSettings[self :: PARAM_MAX2]))
							self :: dieDebug(__METHOD__, "MAX1 or MAX2 are not defined for the limit $encParamName");
						if ($multi)
							self :: dieDebug(__METHOD__, "Multi-values not supported for $encParamName");
						$min = isset ($paramSettings[self :: PARAM_MIN]) ? $paramSettings[self :: PARAM_MIN] : 0;
						$value = intval($value);
						$this->validateLimit($paramName, $value, $min, $paramSettings[self :: PARAM_MAX], $paramSettings[self :: PARAM_MAX2]);
						break;
					case 'boolean' :
						if ($multi)
							self :: dieDebug(__METHOD__, "Multi-values not supported for $encParamName");
						break;
					case 'timestamp' :
						if ($multi)
							self :: dieDebug(__METHOD__, "Multi-values not supported for $encParamName");
						$value = wfTimestamp(TS_UNIX, $value);
						if ($value === 0)
							$this->dieUsage("Invalid value '$value' for timestamp parameter $encParamName", "badtimestamp_{$encParamName}");
						$value = wfTimestamp(TS_MW, $value);
						break;
					case 'user' :
						$title = Title::makeTitleSafe( NS_USER, $value );
						if ( is_null( $title ) )
							$this->dieUsage("Invalid value for user parameter $encParamName", "baduser_{$encParamName}");
						$value = $title->getText();
						break;
					default :
						self :: dieDebug(__METHOD__, "Param $encParamName's type is unknown - $type");
				}
			}

			// There should never be any duplicate values in a list
			if (is_array($value))
				$value = array_unique($value);
		}

		return $value;
	}

	/**
	* Return an array of values that were given in a 'a|b|c' notation,
	* after it optionally validates them against the list allowed values.
	* 
	* @param valueName - The name of the parameter (for error reporting)
	* @param value - The value being parsed
	* @param allowMultiple - Can $value contain more than one value separated by '|'?
	* @param allowedValues - An array of values to check against. If null, all values are accepted.
	* @return (allowMultiple ? an_array_of_values : a_single_value) 
	*/
	protected function parseMultiValue($valueName, $value, $allowMultiple, $allowedValues) 
	{
		$valuesList = explode('|', $value);
		if (!$allowMultiple && count($valuesList) != 1) {
			$possibleValues = is_array($allowedValues) ? "of '" . implode("', '", $allowedValues) . "'" : '';
			$this->dieUsage("Only one $possibleValues is allowed for parameter '$valueName'", "multival_$valueName");
		}
		if (is_array($allowedValues)) {
			$unknownValues = array_diff($valuesList, $allowedValues);
			if ($unknownValues) {
				$this->dieUsage('Unrecognised value' . (count($unknownValues) > 1 ? "s" : "") . " for parameter '$valueName'", "unknown_$valueName");
			}
		}

		return $allowMultiple ? $valuesList : $valuesList[0];
	}

	/**
	* Validate the value against the minimum and user/bot maximum limits. Prints usage info on failure.
	*/
	function validateLimit($paramName, $value, $min, $max, $botMax = null) 
	{
		if (!is_null($min) && $value < $min) {
			$this->dieUsage($this->encodeParamName($paramName) . " may not be less than $min (set to $value)", $paramName);
		}

		// Minimum is always validated, whereas maximum is checked only if not running in internal call mode
		if ($this->getMain()->isInternalMode())
			return;

		// Optimization: do not check user's bot status unless really needed -- skips db query
		// assumes $botMax >= $max
		if (!is_null($max) && $value > $max) {
			if (!is_null($botMax) && ($this->getMain()->isBot() || $this->getMain()->isSysop())) {
				if ($value > $botMax) {
					$this->dieUsage($this->encodeParamName($paramName) . " may not be over $botMax (set to $value) for bots or sysops", $paramName);
				}
			} else {
				$this->dieUsage($this->encodeParamName($paramName) . " may not be over $max (set to $value) for users", $paramName);
			}
		}
	}

	/**
	 * Call main module's error handler 
	 */
	public function dieUsage($description, $errorCode, $httpRespCode = 0) 
	{
		//throw new UsageException($description, $this->encodeParamName($errorCode), $httpRespCode);
	}

	/**
	 * Internal code errors should be reported with this method
	 */
	protected static function dieDebug($method, $message) 
	{
		//wfDebugDieBacktrace("Internal error in $method: $message");
	}

	/**
	 * Profiling: total module execution time
	 */
	private $mTimeIn = 0, $mModuleTime = 0;

	/**
	 * Start module profiling
	 */
	public function profileIn() 
	{
		if ($this->mTimeIn !== 0)
			self :: dieDebug(__METHOD__, 'called twice without calling profileOut()');
		$this->mTimeIn = microtime(true);
		//wfProfileIn($this->getModuleProfileName());
	}

	/**
	 * End module profiling
	 */
	public function profileOut() 
	{
		if ($this->mTimeIn === 0)
			self :: dieDebug(__METHOD__, 'called without calling profileIn() first');
		if ($this->mDBTimeIn !== 0)
			self :: dieDebug(__METHOD__, 'must be called after database profiling is done with profileDBOut()');

		$this->mModuleTime += microtime(true) - $this->mTimeIn;
		$this->mTimeIn = 0;
		//wfProfileOut($this->getModuleProfileName());
	}

	/**
	 * When modules crash, sometimes it is needed to do a profileOut() regardless
	 * of the profiling state the module was in. This method does such cleanup. 
	 */
	public function safeProfileOut() 
	{
		if ($this->mTimeIn !== 0) {
			if ($this->mDBTimeIn !== 0)
				$this->profileDBOut();
			$this->profileOut();
		}
	}

	/**
	 * Total time the module was executed
	 */
	public function getProfileTime() 
	{
		if ($this->mTimeIn !== 0)
			self :: dieDebug(__METHOD__, 'called without calling profileOut() first');
		return $this->mModuleTime;
	}

	/**
	 * Profiling: database execution time
	 */
	private $mDBTimeIn = 0, $mDBTime = 0;

	/**
	 * Start module profiling
	 */
	public function profileDBIn() 
	{
		if ($this->mTimeIn === 0)
			self :: dieDebug(__METHOD__, 'must be called while profiling the entire module with profileIn()');
		if ($this->mDBTimeIn !== 0)
			self :: dieDebug(__METHOD__, 'called twice without calling profileDBOut()');
		$this->mDBTimeIn = microtime(true);
		//wfProfileIn($this->getModuleProfileName(true));
	}

	/**
	 * End database profiling
	 */
	public function profileDBOut() 
	{
		if ($this->mTimeIn === 0)
			self :: dieDebug(__METHOD__, 'must be called while profiling the entire module with profileIn()');
		if ($this->mDBTimeIn === 0)
			self :: dieDebug(__METHOD__, 'called without calling profileDBIn() first');

		$time = microtime(true) - $this->mDBTimeIn;
		$this->mDBTimeIn = 0;

		$this->mDBTime += $time;
		$this->getMain()->mDBTime += $time;
		//wfProfileOut($this->getModuleProfileName(true));
	}

	/**
	 * Total time the module used the database
	 */
	public function getProfileDBTime() 
	{
		if ($this->mDBTimeIn !== 0)
			self :: dieDebug(__METHOD__, 'called without calling profileDBOut() first');
		return $this->mDBTime;
	}
	
	public static function debugPrint($value, $name = 'unknown', $backtrace = false) 
	{
		print "\n\n<pre><b>Debuging value '$name':</b>\n\n";
		var_export($value);
		if ($backtrace)
			print "\n" . wfBacktrace();
		print "\n</pre>\n";
	}

	public abstract function getVersion();

	public static function getBaseVersion() {
		return __CLASS__ . ': $Id$';
	}
}

//</source>