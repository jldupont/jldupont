(function(){var $wnd = window;var $doc = $wnd.document;var $moduleName, $moduleBase;var _,gt='com.google.gwt.core.client.',ht='com.google.gwt.lang.',it='com.google.gwt.user.client.',jt='com.google.gwt.user.client.impl.',kt='com.google.gwt.user.client.ui.',lt='com.google.gwt.user.client.ui.impl.',mt='com.jldupont.project.client.',nt='java.lang.',ot='java.util.';function ft(){}
function yn(a){return this===a;}
function zn(){return ko(this);}
function wn(){}
_=wn.prototype={};_.eQ=yn;_.hC=zn;_.tI=1;var o=null;function r(a){return a==null?0:a.$H?a.$H:(a.$H=t());}
function s(a){return a==null?0:a.$H?a.$H:(a.$H=t());}
function t(){return ++u;}
var u=0;function x(b,a){if(!lb(a,2)){return false;}return B(b,kb(a,2));}
function y(a){return r(a);}
function z(){return [];}
function A(){return {};}
function C(a){return x(this,a);}
function B(a,b){return a===b;}
function D(){return y(this);}
function v(){}
_=v.prototype=new wn();_.eQ=C;_.hC=D;_.tI=7;function F(c,a,d,b,e){c.a=a;c.b=b;e;c.tI=d;return c;}
function bb(a,b,c){return a[b]=c;}
function cb(b,a){return b[a];}
function db(a){return a.length;}
function fb(e,d,c,b,a){return eb(e,d,c,b,0,db(b),a);}
function eb(j,i,g,c,e,a,b){var d,f,h;if((f=cb(c,e))<0){throw new rn();}h=F(new E(),f,cb(i,e),cb(g,e),j);++e;if(e<a){j=ao(j,1);for(d=0;d<f;++d){bb(h,d,eb(j,i,g,c,e,a,b));}}else{for(d=0;d<f;++d){bb(h,d,b);}}return h;}
function gb(a,b,c){if(c!==null&&a.b!=0&& !lb(c,a.b)){throw new Am();}return bb(a,b,c);}
function E(){}
_=E.prototype=new wn();_.tI=0;function jb(b,a){return !(!(b&&ob[b][a]));}
function kb(b,a){if(b!=null)jb(b.tI,a)||nb();return b;}
function lb(b,a){return b!=null&&jb(b.tI,a);}
function nb(){throw new Dm();}
function mb(a){if(a!==null){throw new Dm();}return a;}
function pb(b,d){_=d.prototype;if(b&& !(b.tI>=_.tI)){var c=b.toString;for(var a in _){b[a]=_[a];}b.toString=c;}return b;}
var ob;function mo(b,a){a;return b;}
function lo(){}
_=lo.prototype=new wn();_.tI=3;function cn(b,a){mo(b,a);return b;}
function bn(){}
_=bn.prototype=new lo();_.tI=4;function Bn(b,a){cn(b,a);return b;}
function An(){}
_=An.prototype=new bn();_.tI=5;function tb(b,a){return b;}
function sb(){}
_=sb.prototype=new An();_.tI=8;function jc(a){a.a=xb(new wb(),a);a.b=vq(new tq());a.d=Bb(new Ab(),a);a.f=Fb(new Eb(),a);}
function kc(a){jc(a);return a;}
function mc(c){var a,b,d;a=bc(c.f);ec(c.f);b=null;if(lb(a,4)){b=tb(new sb(),kb(a,4));}else{}if(b!==null){d=o;}pc(c,false);oc(c);}
function nc(e,d){var a,b,c,f;f=false;try{pc(e,true);fc(e.f,e.b.b);re(e.a,10000);while(cc(e.f)){b=dc(e.f);c=true;try{if(b===null){return;}if(lb(b,4)){a=kb(b,4);a.p();}else{}}finally{f=gc(e.f);if(f){return;}if(c){ec(e.f);}}if(sc(jo(),d)){return;}}}finally{if(!f){oe(e.a);pc(e,false);oc(e);}}}
function oc(a){if(!Cq(a.b)&& !a.e&& !a.c){qc(a,true);re(a.d,1);}}
function pc(b,a){b.c=a;}
function qc(b,a){b.e=a;}
function rc(b,a){wq(b.b,a);oc(b);}
function sc(a,b){return qn(a-b)>=100;}
function vb(){}
_=vb.prototype=new wn();_.tI=0;_.c=false;_.e=false;function pe(){pe=ft;xe=vq(new tq());{we();}}
function ne(a){pe();return a;}
function oe(a){if(a.b){se(a.c);}else{te(a.c);}Eq(xe,a);}
function qe(a){if(!a.b){Eq(xe,a);}a.bb();}
function re(b,a){if(a<=0){throw fn(new en(),'must be positive');}oe(b);b.b=false;b.c=ue(b,a);wq(xe,b);}
function se(a){pe();$wnd.clearInterval(a);}
function te(a){pe();$wnd.clearTimeout(a);}
function ue(b,a){pe();return $wnd.setTimeout(function(){b.q();},a);}
function ve(){var a;a=o;{qe(this);}}
function we(){pe();Ce(new je());}
function ie(){}
_=ie.prototype=new wn();_.q=ve;_.tI=9;_.b=false;_.c=0;var xe;function yb(){yb=ft;pe();}
function xb(b,a){yb();b.a=a;ne(b);return b;}
function zb(){if(!this.a.c){return;}mc(this.a);}
function wb(){}
_=wb.prototype=new ie();_.bb=zb;_.tI=10;function Cb(){Cb=ft;pe();}
function Bb(b,a){Cb();b.a=a;ne(b);return b;}
function Db(){qc(this.a,false);nc(this.a,jo());}
function Ab(){}
_=Ab.prototype=new ie();_.bb=Db;_.tI=11;function Fb(b,a){b.d=a;return b;}
function bc(a){return zq(a.d.b,a.b);}
function cc(a){return a.c<a.a;}
function dc(b){var a;b.b=b.c;a=zq(b.d.b,b.c++);if(b.c>=b.a){b.c=0;}return a;}
function ec(a){Dq(a.d.b,a.b);--a.a;if(a.b<=a.c){if(--a.c<0){a.c=0;}}a.b=(-1);}
function fc(b,a){b.a=a;}
function gc(a){return a.b==(-1);}
function hc(){return cc(this);}
function ic(){return dc(this);}
function Eb(){}
_=Eb.prototype=new wn();_.v=hc;_.y=ic;_.tI=0;_.a=0;_.b=(-1);_.c=0;function vc(){vc=ft;qd=vq(new tq());{kd=new kf();tf(kd);}}
function wc(b,a){vc();wf(kd,b,a);}
function xc(a,b){vc();return of(kd,a,b);}
function yc(){vc();return yf(kd,'A');}
function zc(){vc();return yf(kd,'div');}
function Ac(a){vc();return yf(kd,a);}
function Bc(){vc();return yf(kd,'img');}
function Cc(){vc();return zf(kd,'text');}
function Dc(){vc();return yf(kd,'tbody');}
function Ec(){vc();return yf(kd,'tr');}
function Fc(){vc();return yf(kd,'table');}
function cd(b,a,d){vc();var c;c=o;{bd(b,a,d);}}
function bd(b,a,c){vc();var d;if(a===pd){if(ed(b)==8192){pd=null;}}d=ad;ad=b;try{c.z(b);}finally{ad=d;}}
function dd(b,a){vc();Af(kd,b,a);}
function ed(a){vc();return Bf(kd,a);}
function fd(a){vc();pf(kd,a);}
function gd(b,a){vc();return qf(kd,b,a);}
function hd(a){vc();return Cf(kd,a);}
function id(a){vc();return rf(kd,a);}
function jd(a){vc();return sf(kd,a);}
function ld(c,a,b){vc();uf(kd,c,a,b);}
function md(a){vc();var b,c;c=true;if(qd.b>0){b=mb(zq(qd,qd.b-1));if(!(c=null.fb())){dd(a,true);fd(a);}}return c;}
function nd(b,a){vc();Df(kd,b,a);}
function od(b,a){vc();Ef(kd,b,a);}
function rd(b,a,c){vc();Ff(kd,b,a,c);}
function td(a,b,c){vc();bg(kd,a,b,c);}
function sd(a,b,c){vc();ag(kd,a,b,c);}
function ud(a,b){vc();cg(kd,a,b);}
function vd(a,b){vc();dg(kd,a,b);}
function wd(a,b){vc();eg(kd,a,b);}
function xd(b,a,c){vc();fg(kd,b,a,c);}
function yd(a,b){vc();vf(kd,a,b);}
function zd(){vc();return gg(kd);}
function Ad(){vc();return hg(kd);}
var ad=null,kd=null,pd=null,qd;function Cd(){Cd=ft;Ed=kc(new vb());}
function Dd(a){Cd();if(a===null){throw un(new tn(),'cmd can not be null');}rc(Ed,a);}
var Ed;function be(a){if(lb(a,5)){return xc(this,kb(a,5));}return x(pb(this,Fd),a);}
function ce(){return y(pb(this,Fd));}
function Fd(){}
_=Fd.prototype=new v();_.eQ=be;_.hC=ce;_.tI=12;function ge(a){return x(pb(this,de),a);}
function he(){return y(pb(this,de));}
function de(){}
_=de.prototype=new v();_.eQ=ge;_.hC=he;_.tI=13;function le(){while((pe(),xe).b>0){oe(kb(zq((pe(),xe),0),6));}}
function me(){return null;}
function je(){}
_=je.prototype=new wn();_.C=le;_.D=me;_.tI=14;function Be(){Be=ft;De=vq(new tq());hf=vq(new tq());{df();}}
function Ce(a){Be();wq(De,a);}
function Ee(){Be();var a,b;for(a=bp(De);Ao(a);){b=kb(Bo(a),7);b.C();}}
function Fe(){Be();var a,b,c,d;d=null;for(a=bp(De);Ao(a);){b=kb(Bo(a),7);c=b.D();{d=c;}}return d;}
function af(){Be();var a,b;for(a=bp(hf);Ao(a);){b=kb(Bo(a),8);b.E(cf(),bf());}}
function bf(){Be();return zd();}
function cf(){Be();return Ad();}
function df(){Be();__gwt_initHandlers(function(){gf();},function(){return ff();},function(){ef();$wnd.onresize=null;$wnd.onbeforeclose=null;$wnd.onclose=null;});}
function ef(){Be();var a;a=o;{Ee();}}
function ff(){Be();var a;a=o;{return Fe();}}
function gf(){Be();var a;a=o;{af();}}
var De,hf;function wf(c,b,a){b.appendChild(a);}
function yf(b,a){return $doc.createElement(a);}
function zf(b,c){var a=$doc.createElement('INPUT');a.type=c;return a;}
function Af(c,b,a){b.cancelBubble=a;}
function Bf(b,a){switch(a.type){case 'blur':return 4096;case 'change':return 1024;case 'click':return 1;case 'dblclick':return 2;case 'focus':return 2048;case 'keydown':return 128;case 'keypress':return 256;case 'keyup':return 512;case 'load':return 32768;case 'losecapture':return 8192;case 'mousedown':return 4;case 'mousemove':return 64;case 'mouseout':return 32;case 'mouseover':return 16;case 'mouseup':return 8;case 'scroll':return 16384;case 'error':return 65536;case 'mousewheel':return 131072;case 'DOMMouseScroll':return 131072;}}
function Cf(b,a){return a.__eventBits||0;}
function Df(c,b,a){b.removeChild(a);}
function Ef(c,b,a){b.removeAttribute(a);}
function Ff(c,b,a,d){b.setAttribute(a,d);}
function bg(c,a,b,d){a[b]=d;}
function ag(c,a,b,d){a[b]=d;}
function cg(c,a,b){a.__listener=b;}
function dg(c,a,b){a.src=b;}
function eg(c,a,b){if(!b){b='';}a.innerHTML=b;}
function fg(c,b,a,d){b.style[a]=d;}
function gg(a){return $doc.body.clientHeight;}
function hg(a){return $doc.body.clientWidth;}
function jf(){}
_=jf.prototype=new wn();_.tI=0;function of(c,a,b){return a==b;}
function pf(b,a){a.preventDefault();}
function qf(f,c,d){var b=0,a=c.firstChild;while(a){var e=a.nextSibling;if(a.nodeType==1){if(d==b)return a;++b;}a=e;}return null;}
function rf(c,b){var a=b.firstChild;while(a&&a.nodeType!=1)a=a.nextSibling;return a||null;}
function sf(c,a){var b=a.parentNode;if(b==null){return null;}if(b.nodeType!=1)b=null;return b||null;}
function tf(d){$wnd.__dispatchCapturedMouseEvent=function(b){if($wnd.__dispatchCapturedEvent(b)){var a=$wnd.__captureElem;if(a&&a.__listener){cd(b,a,a.__listener);b.stopPropagation();}}};$wnd.__dispatchCapturedEvent=function(a){if(!md(a)){a.stopPropagation();a.preventDefault();return false;}return true;};$wnd.addEventListener('click',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('dblclick',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mousedown',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mouseup',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mousemove',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mousewheel',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('keydown',$wnd.__dispatchCapturedEvent,true);$wnd.addEventListener('keyup',$wnd.__dispatchCapturedEvent,true);$wnd.addEventListener('keypress',$wnd.__dispatchCapturedEvent,true);$wnd.__dispatchEvent=function(b){var c,a=this;while(a&& !(c=a.__listener))a=a.parentNode;if(a&&a.nodeType!=1)a=null;if(c)cd(b,a,c);};$wnd.__captureElem=null;}
function uf(f,e,g,d){var c=0,b=e.firstChild,a=null;while(b){if(b.nodeType==1){if(c==d){a=b;break;}++c;}b=b.nextSibling;}e.insertBefore(g,a);}
function vf(c,b,a){b.__eventBits=a;b.onclick=a&1?$wnd.__dispatchEvent:null;b.ondblclick=a&2?$wnd.__dispatchEvent:null;b.onmousedown=a&4?$wnd.__dispatchEvent:null;b.onmouseup=a&8?$wnd.__dispatchEvent:null;b.onmouseover=a&16?$wnd.__dispatchEvent:null;b.onmouseout=a&32?$wnd.__dispatchEvent:null;b.onmousemove=a&64?$wnd.__dispatchEvent:null;b.onkeydown=a&128?$wnd.__dispatchEvent:null;b.onkeypress=a&256?$wnd.__dispatchEvent:null;b.onkeyup=a&512?$wnd.__dispatchEvent:null;b.onchange=a&1024?$wnd.__dispatchEvent:null;b.onfocus=a&2048?$wnd.__dispatchEvent:null;b.onblur=a&4096?$wnd.__dispatchEvent:null;b.onlosecapture=a&8192?$wnd.__dispatchEvent:null;b.onscroll=a&16384?$wnd.__dispatchEvent:null;b.onload=a&32768?$wnd.__dispatchEvent:null;b.onerror=a&65536?$wnd.__dispatchEvent:null;b.onmousewheel=a&131072?$wnd.__dispatchEvent:null;}
function mf(){}
_=mf.prototype=new jf();_.tI=0;function kf(){}
_=kf.prototype=new mf();_.tI=0;function wk(d,b,a){var c=b.parentNode;if(!c){return;}c.insertBefore(a,b);c.removeChild(b);}
function xk(b,a){if(b.h!==null){wk(b,b.h,a);}b.h=a;}
function yk(b,a){xd(b.h,'height',a);}
function zk(b,c,a){Dk(b,c);yk(b,a);}
function Ak(b,a){Fk(b.h,a);}
function Bk(b,a){al(b.h,a);}
function Ck(a,b){if(b===null||Fn(b)==0){od(a.h,'title');}else{rd(a.h,'title',b);}}
function Dk(a,b){xd(a.h,'width',b);}
function Ek(b,a){yd(b.h,a|hd(b.h));}
function Fk(a,b){td(a,'className',b);}
function al(a,b){if(a===null){throw Bn(new An(),'Null widget handle. If you are creating a composite, ensure that initWidget() has been called.');}b=bo(b);if(Fn(b)==0){throw fn(new en(),'Style names cannot be empty');}bl(a,b);}
function bl(b,f){var a=b.className.split(/\s+/);if(!a){return;}var g=a[0];var h=g.length;a[0]=f;for(var c=1,d=a.length;c<d;c++){var e=a[c];if(e.length>h&&(e.charAt(h)=='-'&&e.indexOf(g)==0)){a[c]=f+e.substring(h);}}b.className=a.join(' ');}
function uk(){}
_=uk.prototype=new wn();_.tI=0;_.h=null;function sl(a){if(a.f){throw jn(new hn(),"Should only call onAttach when the widget is detached from the browser's document");}a.f=true;ud(a.h,a);a.m();a.A();}
function tl(a){if(!a.f){throw jn(new hn(),"Should only call onDetach when the widget is attached to the browser's document");}try{a.B();}finally{a.n();ud(a.h,null);a.f=false;}}
function ul(a){if(a.g!==null){a.g.ab(a);}else if(a.g!==null){throw jn(new hn(),"This widget's parent does not implement HasWidgets");}}
function vl(b,a){if(b.f){ud(b.h,null);}xk(b,a);if(b.f){ud(a,b);}}
function wl(c,b){var a;a=c.g;if(b===null){if(a!==null&&a.f){tl(c);}c.g=null;}else{if(a!==null){throw jn(new hn(),'Cannot set a new parent without first clearing the old parent');}c.g=b;if(b.f){sl(c);}}}
function xl(){}
function yl(){}
function zl(a){}
function Al(){}
function Bl(){}
function Cl(a){vl(this,a);}
function cl(){}
_=cl.prototype=new uk();_.m=xl;_.n=yl;_.z=zl;_.A=Al;_.B=Bl;_.cb=Cl;_.tI=15;_.f=false;_.g=null;function pj(b,a){wl(a,b);}
function rj(b,a){wl(a,null);}
function sj(){var a,b;for(b=this.w();b.v();){a=kb(b.y(),9);sl(a);}}
function tj(){var a,b;for(b=this.w();b.v();){a=kb(b.y(),9);tl(a);}}
function uj(){}
function vj(){}
function oj(){}
_=oj.prototype=new cl();_.m=sj;_.n=tj;_.A=uj;_.B=vj;_.tI=16;function rg(a){a.a=jl(new dl(),a);}
function sg(a){rg(a);return a;}
function tg(c,a,b){ul(a);kl(c.a,a);wc(b,a.h);pj(c,a);}
function vg(b,c){var a;if(c.g!==b){return false;}rj(b,c);a=c.h;nd(jd(a),a);ql(b.a,c);return true;}
function wg(){return ol(this.a);}
function xg(a){return vg(this,a);}
function qg(){}
_=qg.prototype=new oj();_.w=wg;_.ab=xg;_.tI=17;function jg(a){sg(a);a.cb(zc());xd(a.h,'position','relative');xd(a.h,'overflow','hidden');return a;}
function kg(a,b){tg(a,b,a.h);}
function lg(b,d,a,c){ul(d);ng(b,d,a,c);kg(b,d);}
function ng(c,e,b,d){var a;a=e.h;if(b==(-1)&&d==(-1)){og(a);}else{xd(a,'position','absolute');xd(a,'left',b+'px');xd(a,'top',d+'px');}}
function og(a){xd(a,'left','');xd(a,'top','');xd(a,'position','');}
function pg(b){var a;a=vg(this,b);if(a){og(b.h);}return a;}
function ig(){}
_=ig.prototype=new qg();_.ab=pg;_.tI=18;function pi(a){a.e=fi(new ai());}
function qi(a){pi(a);a.d=Fc();a.a=Dc();wc(a.d,a.a);a.cb(a.d);Ek(a,1);return a;}
function ri(c,a){var b;b=ah(c);if(a>=b||a<0){throw mn(new ln(),'Row index: '+a+', Row size: '+b);}}
function si(e,c,b,a){var d;d=Ah(e.b,c,b);yi(e,d,a);return d;}
function ui(c,b,a){return b.rows[a].cells.length;}
function vi(a){return wi(a,a.a);}
function wi(b,a){return a.rows.length;}
function xi(b,a){var c;if(a!=ah(b)){ri(b,a);}c=Ec();ld(b.a,c,a);return a;}
function yi(d,c,a){var b,e;b=id(c);e=null;if(b!==null){e=hi(d.e,b);}if(e!==null){zi(d,e);return true;}else{if(a){wd(c,'');}return false;}}
function zi(b,c){var a;if(c.g!==b){return false;}rj(b,c);a=c.h;nd(jd(a),a);ki(b.e,a);return true;}
function Ai(a,b){td(a.d,'border',''+b);}
function Bi(b,a){b.b=a;}
function Ci(b,a){sd(b.d,'cellPadding',a);}
function Di(b,a){sd(b.d,'cellSpacing',a);}
function Ei(b,a){b.c=a;Fh(b.c);}
function Fi(d,b,a,e){var c;ch(d,b,a);if(e!==null){ul(e);c=si(d,b,a,true);ii(d.e,e);wc(c,e.h);pj(d,e);}}
function aj(){return li(this.e);}
function bj(a){switch(ed(a)){case 1:{break;}default:}}
function cj(a){return zi(this,a);}
function mh(){}
_=mh.prototype=new oj();_.w=aj;_.z=bj;_.ab=cj;_.tI=19;_.a=null;_.b=null;_.c=null;_.d=null;function Dg(a){qi(a);Bi(a,Ag(new zg(),a));Ei(a,Dh(new Ch(),a));return a;}
function Fg(b,a){ri(b,a);return ui(b,b.a,a);}
function ah(a){return vi(a);}
function bh(b,a){return xi(b,a);}
function ch(e,d,b){var a,c;dh(e,d);if(b<0){throw mn(new ln(),'Cannot create a column with a negative index: '+b);}a=Fg(e,d);c=b+1-a;if(c>0){eh(e.a,d,c);}}
function dh(d,b){var a,c;if(b<0){throw mn(new ln(),'Cannot create a row with a negative index: '+b);}c=ah(d);for(a=c;a<=b;a++){bh(d,a);}}
function eh(f,d,c){var e=f.rows[d];for(var b=0;b<c;b++){var a=$doc.createElement('td');e.appendChild(a);}}
function yg(){}
_=yg.prototype=new mh();_.tI=20;function wh(b,a){b.a=a;return b;}
function yh(c,b,a){ch(c.a,b,a);return zh(c,c.a.a,b,a);}
function zh(e,d,c,a){var b=d.rows[c].cells[a];return b==null?null:b;}
function Ah(c,b,a){return zh(c,c.a.a,b,a);}
function Bh(e,d,b,a){var c;ch(e.a,d,b);c=zh(e,e.a.a,d,b);td(c,'align',a.a);}
function vh(){}
_=vh.prototype=new wn();_.tI=0;function Ag(b,a){wh(b,a);return b;}
function Cg(d,c,b,a){sd(yh(d,c,b),'colSpan',a);}
function zg(){}
_=zg.prototype=new vh();_.tI=0;function hh(){hh=ft;gm(),im;}
function gh(b,a){gm(),im;jh(b,a);return b;}
function ih(b,a){switch(ed(a)){case 1:break;case 4096:case 2048:break;case 128:case 512:case 256:break;}}
function jh(b,a){vl(b,a);Ek(b,7041);}
function kh(a){ih(this,a);}
function lh(a){jh(this,a);}
function fh(){}
_=fh.prototype=new cl();_.z=kh;_.cb=lh;_.tI=21;function oh(a){{rh(a);}}
function ph(b,a){b.b=a;oh(b);return b;}
function rh(a){while(++a.a<a.b.b.b){if(zq(a.b.b,a.a)!==null){return;}}}
function sh(a){return a.a<a.b.b.b;}
function th(){return sh(this);}
function uh(){var a;if(!sh(this)){throw new bt();}a=zq(this.b.b,this.a);rh(this);return a;}
function nh(){}
_=nh.prototype=new wn();_.v=th;_.y=uh;_.tI=0;_.a=(-1);function Dh(b,a){b.b=a;return b;}
function Fh(a){if(a.a===null){a.a=Ac('colgroup');ld(a.b.d,a.a,0);wc(a.a,Ac('col'));}}
function Ch(){}
_=Ch.prototype=new wn();_.tI=0;_.a=null;function ei(a){a.b=vq(new tq());}
function fi(a){ei(a);return a;}
function hi(c,a){var b;b=ni(a);if(b<0){return null;}return kb(zq(c.b,b),9);}
function ii(b,c){var a;if(b.a===null){a=b.b.b;wq(b.b,c);}else{a=b.a.a;Fq(b.b,a,c);b.a=b.a.b;}oi(c.h,a);}
function ji(c,a,b){mi(a);Fq(c.b,b,null);c.a=ci(new bi(),b,c.a);}
function ki(c,a){var b;b=ni(a);ji(c,a,b);}
function li(a){return ph(new nh(),a);}
function mi(a){a['__widgetID']=null;}
function ni(a){var b=a['__widgetID'];return b==null?-1:b;}
function oi(a,b){a['__widgetID']=b;}
function ai(){}
_=ai.prototype=new wn();_.tI=0;_.a=null;function ci(c,a,b){c.a=a;c.b=b;return c;}
function bi(){}
_=bi.prototype=new wn();_.tI=0;_.a=0;_.b=null;function ij(){ij=ft;jj=gj(new fj(),'center');gj(new fj(),'left');gj(new fj(),'right');}
var jj;function gj(b,a){b.a=a;return b;}
function fj(){}
_=fj.prototype=new wn();_.tI=0;_.a=null;function Cj(){Cj=ft;bk=gs(new nr());}
function Bj(b,a){Cj();jg(b);if(a===null){a=Dj();}b.cb(a);sl(b);return b;}
function Ej(){Cj();return Fj(null);}
function Fj(c){Cj();var a,b;b=kb(ms(bk,c),10);if(b!==null){return b;}a=null;if(bk.c==0){ak();}ns(bk,c,b=Bj(new wj(),a));return b;}
function Dj(){Cj();return $doc.body;}
function ak(){Cj();Ce(new xj());}
function wj(){}
_=wj.prototype=new ig();_.tI=22;var bk;function zj(){var a,b;for(b=Ap(iq((Cj(),bk)));bq(b);){a=kb(cq(b),10);if(a.f){tl(a);}}}
function Aj(){return null;}
function xj(){}
_=xj.prototype=new wn();_.C=zj;_.D=Aj;_.tI=23;function nk(){nk=ft;gm(),im;qk=kk(new jk(),'center');kk(new jk(),'justify');kk(new jk(),'left');kk(new jk(),'right');}
function mk(b,a){nk();gh(b,a);Ek(b,1024);return b;}
function pk(b,a){td(b.h,'value',a!==null?a:'');}
function ok(b,a){xd(b.h,'textAlign',a.a);}
function rk(a){var b;ih(this,a);b=ed(a);}
function ik(){}
_=ik.prototype=new fh();_.z=rk;_.tI=24;var qk;function tk(){tk=ft;nk();}
function sk(a){tk();mk(a,Cc());Ak(a,'gwt-TextBox');return a;}
function hk(){}
_=hk.prototype=new ik();_.tI=25;function kk(b,a){b.a=a;return b;}
function jk(){}
_=jk.prototype=new wn();_.tI=0;_.a=null;function jl(b,a){b.a=fb('[Lcom.google.gwt.user.client.ui.Widget;',[0],[9],[4],null);return b;}
function kl(a,b){nl(a,b,a.b);}
function ml(b,c){var a;for(a=0;a<b.b;++a){if(b.a[a]===c){return a;}}return (-1);}
function nl(d,e,a){var b,c;if(a<0||a>d.b){throw new ln();}if(d.b==d.a.a){c=fb('[Lcom.google.gwt.user.client.ui.Widget;',[0],[9],[d.a.a*2],null);for(b=0;b<d.a.a;++b){gb(c,b,d.a[b]);}d.a=c;}++d.b;for(b=d.b-1;b>a;--b){gb(d.a,b,d.a[b-1]);}gb(d.a,a,e);}
function ol(a){return fl(new el(),a);}
function pl(c,b){var a;if(b<0||b>=c.b){throw new ln();}--c.b;for(a=b;a<c.b;++a){gb(c.a,a,c.a[a+1]);}gb(c.a,c.b,null);}
function ql(b,c){var a;a=ml(b,c);if(a==(-1)){throw new bt();}pl(b,a);}
function dl(){}
_=dl.prototype=new wn();_.tI=0;_.a=null;_.b=0;function fl(b,a){b.b=a;return b;}
function hl(){return this.a<this.b.b-1;}
function il(){if(this.a>=this.b.b){throw new bt();}return this.b.a[++this.a];}
function el(){}
_=el.prototype=new wn();_.v=hl;_.y=il;_.tI=0;_.a=(-1);function gm(){gm=ft;hm=am(new El());im=hm!==null?fm(new Dl()):hm;}
function fm(a){gm();return a;}
function Dl(){}
_=Dl.prototype=new wn();_.tI=0;var hm,im;function bm(){bm=ft;gm();}
function Fl(a){cm(a);dm(a);em(a);}
function am(a){bm();fm(a);Fl(a);return a;}
function cm(b){return function(a){if(this.parentNode.onblur){this.parentNode.onblur(a);}};}
function dm(b){return function(a){if(this.parentNode.onfocus){this.parentNode.onfocus(a);}};}
function em(a){return function(){this.firstChild.focus();};}
function El(){}
_=El.prototype=new Dl();_.tI=0;function km(a){a.cb(yc());return a;}
function mm(b,a){rd(b.h,'href',a===null?'':a);}
function nm(b,a){rd(b.h,'id',a===null?'':a);}
function om(c,d){var a,b;a=c.h;b=gd(a,0);if(b===null){b=Bc();ld(a,b,0);}vd(b,d);}
function pm(b,a){rd(b.h,'target',a===null?'':a);}
function jm(){}
_=jm.prototype=new cl();_.tI=26;function um(a){a.f=Dg(new yg());a.b=km(new jm());a.a=km(new jm());a.d=km(new jm());a.c=km(new jm());a.e=sk(new hk());}
function wm(a){um(a);return a;}
function xm(b){var a;Ej();a=Ej();zk(a,'100%','100%');Bk(a,'rootPanel');Ak(a,'rootPanel');lg(a,b.f,60,0);Ai(b.f,2);zk(b.f,'377px','270px');Di(b.f,5);Ci(b.f,5);Fi(b.f,1,0,b.b);Bh(b.f.b,1,0,(ij(),jj));pm(b.b,'_blank');mm(b.b,'http://www.linkedin.com/in/JeanLouDupont');nm(b.b,'link_linkedin');om(b.b,'linkedin.gif');Fi(b.f,1,1,b.a);Bh(b.f.b,1,1,(ij(),jj));pm(b.a,'_blank');mm(b.a,'http://jldupont.blogspot.com');nm(b.a,'link_blog');om(b.a,'blog.jpg');Fi(b.f,2,0,b.d);Bh(b.f.b,2,0,(ij(),jj));pm(b.d,'_blank');mm(b.d,'http://wiki.jldupont.com');nm(b.d,'link_wiki');om(b.d,'wiki.png');Fi(b.f,2,1,b.c);Bh(b.f.b,2,1,(ij(),jj));pm(b.c,'_blank');mm(b.c,'http://code.google.com/u/JeanLou.Dupont/');nm(b.c,'link_projects');om(b.c,'projects.jpg');Fi(b.f,0,0,b.e);Ak(b.e,'title');ok(b.e,(nk(),qk));Ck(b.e,'title');Bh(b.f.b,0,0,(ij(),jj));pk(b.e,"Jean-Lou Dupont's WEB site");Cg(b.f.b,0,0,2);Dk(b.e,'100%');Dd(new rm());cf(),bf();}
function ym(b,a){}
function qm(){}
_=qm.prototype=new wn();_.E=ym;_.tI=27;function tm(){cf(),bf();}
function rm(){}
_=rm.prototype=new wn();_.p=tm;_.tI=28;function Am(){}
_=Am.prototype=new An();_.tI=29;function Dm(){}
_=Dm.prototype=new An();_.tI=30;function fn(b,a){Bn(b,a);return b;}
function en(){}
_=en.prototype=new An();_.tI=31;function jn(b,a){Bn(b,a);return b;}
function hn(){}
_=hn.prototype=new An();_.tI=32;function mn(b,a){Bn(b,a);return b;}
function ln(){}
_=ln.prototype=new An();_.tI=33;function qn(a){return a<0?-a:a;}
function rn(){}
_=rn.prototype=new An();_.tI=34;function un(b,a){Bn(b,a);return b;}
function tn(){}
_=tn.prototype=new An();_.tI=35;function Fn(a){return a.length;}
function ao(b,a){return b.substr(a,b.length-a);}
function bo(c){var a=c.replace(/^(\s*)/,'');var b=a.replace(/\s*$/,'');return b;}
function co(a,b){return String(a)==b;}
function eo(a){if(!lb(a,1))return false;return co(this,a);}
function go(){var a=fo;if(!a){a=fo={};}var e=':'+this;var b=a[e];if(b==null){b=0;var f=this.length;var d=f<64?1:f/32|0;for(var c=0;c<f;c+=d){b<<=1;b+=this.charCodeAt(c);}b|=0;a[e]=b;}return b;}
_=String.prototype;_.eQ=eo;_.hC=go;_.tI=2;var fo=null;function jo(){return new Date().getTime();}
function ko(a){return s(a);}
function po(b,a){Bn(b,a);return b;}
function oo(){}
_=oo.prototype=new An();_.tI=36;function so(d,a,b){var c;while(a.v()){c=a.y();if(b===null?c===null:b.eQ(c)){return a;}}return null;}
function uo(a){throw po(new oo(),'add');}
function vo(b){var a;a=so(this,this.w(),b);return a!==null;}
function ro(){}
_=ro.prototype=new wn();_.j=uo;_.l=vo;_.tI=0;function ap(b,a){throw mn(new ln(),'Index: '+a+', Size: '+b.b);}
function bp(a){return yo(new xo(),a);}
function cp(b,a){throw po(new oo(),'add');}
function dp(a){this.i(this.db(),a);return true;}
function ep(e){var a,b,c,d,f;if(e===this){return true;}if(!lb(e,14)){return false;}f=kb(e,14);if(this.db()!=f.db()){return false;}c=bp(this);d=f.w();while(Ao(c)){a=Bo(c);b=Bo(d);if(!(a===null?b===null:a.eQ(b))){return false;}}return true;}
function fp(){var a,b,c,d;c=1;a=31;b=bp(this);while(Ao(b)){d=Bo(b);c=31*c+(d===null?0:d.hC());}return c;}
function gp(){return bp(this);}
function hp(a){throw po(new oo(),'remove');}
function wo(){}
_=wo.prototype=new ro();_.i=cp;_.j=dp;_.eQ=ep;_.hC=fp;_.w=gp;_.F=hp;_.tI=37;function yo(b,a){b.c=a;return b;}
function Ao(a){return a.a<a.c.db();}
function Bo(a){if(!Ao(a)){throw new bt();}return a.c.t(a.b=a.a++);}
function Co(a){if(a.b<0){throw new hn();}a.c.F(a.b);a.a=a.b;a.b=(-1);}
function Do(){return Ao(this);}
function Eo(){return Bo(this);}
function xo(){}
_=xo.prototype=new wn();_.v=Do;_.y=Eo;_.tI=0;_.a=0;_.b=(-1);function gq(f,d,e){var a,b,c;for(b=bs(f.o());Ar(b);){a=Br(b);c=a.r();if(d===null?c===null:d.eQ(c)){if(e){Cr(b);}return a;}}return null;}
function hq(b){var a;a=b.o();return kp(new jp(),b,a);}
function iq(b){var a;a=ls(b);return yp(new xp(),b,a);}
function jq(a){return gq(this,a,false)!==null;}
function kq(d){var a,b,c,e,f,g,h;if(d===this){return true;}if(!lb(d,15)){return false;}f=kb(d,15);c=hq(this);e=f.x();if(!qq(c,e)){return false;}for(a=mp(c);tp(a);){b=up(a);h=this.u(b);g=f.u(b);if(h===null?g!==null:!h.eQ(g)){return false;}}return true;}
function lq(b){var a;a=gq(this,b,false);return a===null?null:a.s();}
function mq(){var a,b,c;b=0;for(c=bs(this.o());Ar(c);){a=Br(c);b+=a.hC();}return b;}
function nq(){return hq(this);}
function ip(){}
_=ip.prototype=new wn();_.k=jq;_.eQ=kq;_.u=lq;_.hC=mq;_.x=nq;_.tI=38;function qq(e,b){var a,c,d;if(b===e){return true;}if(!lb(b,16)){return false;}c=kb(b,16);if(c.db()!=e.db()){return false;}for(a=c.w();a.v();){d=a.y();if(!e.l(d)){return false;}}return true;}
function rq(a){return qq(this,a);}
function sq(){var a,b,c;a=0;for(b=this.w();b.v();){c=b.y();if(c!==null){a+=c.hC();}}return a;}
function oq(){}
_=oq.prototype=new ro();_.eQ=rq;_.hC=sq;_.tI=39;function kp(b,a,c){b.a=a;b.b=c;return b;}
function mp(b){var a;a=bs(b.b);return rp(new qp(),b,a);}
function np(a){return this.a.k(a);}
function op(){return mp(this);}
function pp(){return this.b.a.c;}
function jp(){}
_=jp.prototype=new oq();_.l=np;_.w=op;_.db=pp;_.tI=40;function rp(b,a,c){b.a=c;return b;}
function tp(a){return a.a.v();}
function up(b){var a;a=b.a.y();return a.r();}
function vp(){return tp(this);}
function wp(){return up(this);}
function qp(){}
_=qp.prototype=new wn();_.v=vp;_.y=wp;_.tI=0;function yp(b,a,c){b.a=a;b.b=c;return b;}
function Ap(b){var a;a=bs(b.b);return Fp(new Ep(),b,a);}
function Bp(a){return ks(this.a,a);}
function Cp(){return Ap(this);}
function Dp(){return this.b.a.c;}
function xp(){}
_=xp.prototype=new ro();_.l=Bp;_.w=Cp;_.db=Dp;_.tI=0;function Fp(b,a,c){b.a=c;return b;}
function bq(a){return a.a.v();}
function cq(a){var b;b=a.a.y().s();return b;}
function dq(){return bq(this);}
function eq(){return cq(this);}
function Ep(){}
_=Ep.prototype=new wn();_.v=dq;_.y=eq;_.tI=0;function uq(a){{xq(a);}}
function vq(a){uq(a);return a;}
function wq(b,a){jr(b.a,b.b++,a);return true;}
function xq(a){a.a=z();a.b=0;}
function zq(b,a){if(a<0||a>=b.b){ap(b,a);}return fr(b.a,a);}
function Aq(b,a){return Bq(b,a,0);}
function Bq(c,b,a){if(a<0){ap(c,a);}for(;a<c.b;++a){if(er(b,fr(c.a,a))){return a;}}return (-1);}
function Cq(a){return a.b==0;}
function Dq(c,a){var b;b=zq(c,a);hr(c.a,a,1);--c.b;return b;}
function Eq(c,b){var a;a=Aq(c,b);if(a==(-1)){return false;}Dq(c,a);return true;}
function Fq(d,a,b){var c;c=zq(d,a);jr(d.a,a,b);return c;}
function br(a,b){if(a<0||a>this.b){ap(this,a);}ar(this.a,a,b);++this.b;}
function cr(a){return wq(this,a);}
function ar(a,b,c){a.splice(b,0,c);}
function dr(a){return Aq(this,a)!=(-1);}
function er(a,b){return a===b||a!==null&&a.eQ(b);}
function gr(a){return zq(this,a);}
function fr(a,b){return a[b];}
function ir(a){return Dq(this,a);}
function hr(a,c,b){a.splice(c,b);}
function jr(a,b,c){a[b]=c;}
function kr(){return this.b;}
function tq(){}
_=tq.prototype=new wo();_.i=br;_.j=cr;_.l=dr;_.t=gr;_.F=ir;_.db=kr;_.tI=41;_.a=null;_.b=0;function is(){is=ft;ps=vs();}
function fs(a){{hs(a);}}
function gs(a){is();fs(a);return a;}
function hs(a){a.a=z();a.d=A();a.b=pb(ps,v);a.c=0;}
function js(b,a){if(lb(a,1)){return zs(b.d,kb(a,1))!==ps;}else if(a===null){return b.b!==ps;}else{return ys(b.a,a,a.hC())!==ps;}}
function ks(a,b){if(a.b!==ps&&xs(a.b,b)){return true;}else if(us(a.d,b)){return true;}else if(ss(a.a,b)){return true;}return false;}
function ls(a){return Fr(new wr(),a);}
function ms(c,a){var b;if(lb(a,1)){b=zs(c.d,kb(a,1));}else if(a===null){b=c.b;}else{b=ys(c.a,a,a.hC());}return b===ps?null:b;}
function ns(c,a,d){var b;{b=c.b;c.b=d;}if(b===ps){++c.c;return null;}else{return b;}}
function os(c,a){var b;if(lb(a,1)){b=Cs(c.d,kb(a,1));}else if(a===null){b=c.b;c.b=pb(ps,v);}else{b=Bs(c.a,a,a.hC());}if(b===ps){return null;}else{--c.c;return b;}}
function qs(e,c){is();for(var d in e){if(d==parseInt(d)){var a=e[d];for(var f=0,b=a.length;f<b;++f){c.j(a[f]);}}}}
function rs(d,a){is();for(var c in d){if(c.charCodeAt(0)==58){var e=d[c];var b=rr(c.substring(1),e);a.j(b);}}}
function ss(f,h){is();for(var e in f){if(e==parseInt(e)){var a=f[e];for(var g=0,b=a.length;g<b;++g){var c=a[g];var d=c.s();if(xs(h,d)){return true;}}}}return false;}
function ts(a){return js(this,a);}
function us(c,d){is();for(var b in c){if(b.charCodeAt(0)==58){var a=c[b];if(xs(d,a)){return true;}}}return false;}
function vs(){is();}
function ws(){return ls(this);}
function xs(a,b){is();if(a===b){return true;}else if(a===null){return false;}else{return a.eQ(b);}}
function As(a){return ms(this,a);}
function ys(f,h,e){is();var a=f[e];if(a){for(var g=0,b=a.length;g<b;++g){var c=a[g];var d=c.r();if(xs(h,d)){return c.s();}}}}
function zs(b,a){is();return b[':'+a];}
function Bs(f,h,e){is();var a=f[e];if(a){for(var g=0,b=a.length;g<b;++g){var c=a[g];var d=c.r();if(xs(h,d)){if(a.length==1){delete f[e];}else{a.splice(g,1);}return c.s();}}}}
function Cs(c,a){is();a=':'+a;var b=c[a];delete c[a];return b;}
function nr(){}
_=nr.prototype=new ip();_.k=ts;_.o=ws;_.u=As;_.tI=42;_.a=null;_.b=null;_.c=0;_.d=null;var ps;function pr(b,a,c){b.a=a;b.b=c;return b;}
function rr(a,b){return pr(new or(),a,b);}
function sr(b){var a;if(lb(b,17)){a=kb(b,17);if(xs(this.a,a.r())&&xs(this.b,a.s())){return true;}}return false;}
function tr(){return this.a;}
function ur(){return this.b;}
function vr(){var a,b;a=0;b=0;if(this.a!==null){a=this.a.hC();}if(this.b!==null){b=this.b.hC();}return a^b;}
function or(){}
_=or.prototype=new wn();_.eQ=sr;_.r=tr;_.s=ur;_.hC=vr;_.tI=43;_.a=null;_.b=null;function Fr(b,a){b.a=a;return b;}
function bs(a){return yr(new xr(),a.a);}
function cs(c){var a,b,d;if(lb(c,17)){a=kb(c,17);b=a.r();if(js(this.a,b)){d=ms(this.a,b);return xs(a.s(),d);}}return false;}
function ds(){return bs(this);}
function es(){return this.a.c;}
function wr(){}
_=wr.prototype=new oq();_.l=cs;_.w=ds;_.db=es;_.tI=44;function yr(c,b){var a;c.c=b;a=vq(new tq());if(c.c.b!==(is(),ps)){wq(a,pr(new or(),null,c.c.b));}rs(c.c.d,a);qs(c.c.a,a);c.a=bp(a);return c;}
function Ar(a){return Ao(a.a);}
function Br(a){return a.b=kb(Bo(a.a),17);}
function Cr(a){if(a.b===null){throw jn(new hn(),'Must call next() before remove().');}else{Co(a.a);os(a.c,a.b.r());a.b=null;}}
function Dr(){return Ar(this);}
function Er(){return Br(this);}
function xr(){}
_=xr.prototype=new wn();_.v=Dr;_.y=Er;_.tI=0;_.a=null;_.b=null;function bt(){}
_=bt.prototype=new An();_.tI=45;function zm(){xm(wm(new qm()));km(new jm());}
function gwtOnLoad(b,d,c){$moduleName=d;$moduleBase=c;if(b)try{zm();}catch(a){b(d);}else{zm();}}
var ob=[{},{},{1:1},{3:1},{3:1},{3:1},{3:1},{2:1},{3:1},{6:1},{6:1},{6:1},{2:1,5:1},{2:1},{7:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,10:1,11:1,12:1,13:1},{7:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{8:1},{4:1},{3:1},{3:1},{3:1},{3:1},{3:1},{3:1},{3:1},{3:1},{14:1},{15:1},{16:1},{16:1},{14:1},{15:1},{17:1},{16:1},{3:1}];if (com_jldupont_project_main) {  var __gwt_initHandlers = com_jldupont_project_main.__gwt_initHandlers;  com_jldupont_project_main.onScriptLoad(gwtOnLoad);}})();