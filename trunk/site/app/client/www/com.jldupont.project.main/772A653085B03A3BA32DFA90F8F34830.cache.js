(function(){var $wnd = window;var $doc = $wnd.document;var $moduleName, $moduleBase;var _,zt='com.google.gwt.core.client.',At='com.google.gwt.lang.',Bt='com.google.gwt.user.client.',Ct='com.google.gwt.user.client.impl.',Dt='com.google.gwt.user.client.ui.',Et='com.google.gwt.user.client.ui.impl.',Ft='com.jldupont.project.client.',au='java.lang.',bu='java.util.';function yt(){}
function mo(a){return this===a;}
function no(){return Do(this);}
function ko(){}
_=ko.prototype={};_.eQ=mo;_.hC=no;_.tI=1;var o=null;function r(a){return a==null?0:a.$H?a.$H:(a.$H=t());}
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
_=v.prototype=new ko();_.eQ=C;_.hC=D;_.tI=7;function F(c,a,d,b,e){c.a=a;c.b=b;e;c.tI=d;return c;}
function bb(a,b,c){return a[b]=c;}
function cb(b,a){return b[a];}
function db(a){return a.length;}
function fb(e,d,c,b,a){return eb(e,d,c,b,0,db(b),a);}
function eb(j,i,g,c,e,a,b){var d,f,h;if((f=cb(c,e))<0){throw new fo();}h=F(new E(),f,cb(i,e),cb(g,e),j);++e;if(e<a){j=uo(j,1);for(d=0;d<f;++d){bb(h,d,eb(j,i,g,c,e,a,b));}}else{for(d=0;d<f;++d){bb(h,d,b);}}return h;}
function gb(a,b,c){if(c!==null&&a.b!=0&& !lb(c,a.b)){throw new on();}return bb(a,b,c);}
function E(){}
_=E.prototype=new ko();_.tI=0;function jb(b,a){return !(!(b&&ob[b][a]));}
function kb(b,a){if(b!=null)jb(b.tI,a)||nb();return b;}
function lb(b,a){return b!=null&&jb(b.tI,a);}
function nb(){throw new rn();}
function mb(a){if(a!==null){throw new rn();}return a;}
function pb(b,d){_=d.prototype;if(b&& !(b.tI>=_.tI)){var c=b.toString;for(var a in _){b[a]=_[a];}b.toString=c;}return b;}
var ob;function Fo(b,a){a;return b;}
function Eo(){}
_=Eo.prototype=new ko();_.tI=3;function wn(b,a){Fo(b,a);return b;}
function vn(){}
_=vn.prototype=new Eo();_.tI=4;function po(b,a){wn(b,a);return b;}
function oo(){}
_=oo.prototype=new vn();_.tI=5;function tb(b,a){return b;}
function sb(){}
_=sb.prototype=new oo();_.tI=8;function jc(a){a.a=xb(new wb(),a);a.b=ir(new gr());a.d=Bb(new Ab(),a);a.f=Fb(new Eb(),a);}
function kc(a){jc(a);return a;}
function mc(c){var a,b,d;a=bc(c.f);ec(c.f);b=null;if(lb(a,4)){b=tb(new sb(),kb(a,4));}else{}if(b!==null){d=o;}pc(c,false);oc(c);}
function nc(e,d){var a,b,c,f;f=false;try{pc(e,true);fc(e.f,e.b.b);re(e.a,10000);while(cc(e.f)){b=dc(e.f);c=true;try{if(b===null){return;}if(lb(b,4)){a=kb(b,4);a.p();}else{}}finally{f=gc(e.f);if(f){return;}if(c){ec(e.f);}}if(sc(Co(),d)){return;}}}finally{if(!f){oe(e.a);pc(e,false);oc(e);}}}
function oc(a){if(!pr(a.b)&& !a.e&& !a.c){qc(a,true);re(a.d,1);}}
function pc(b,a){b.c=a;}
function qc(b,a){b.e=a;}
function rc(b,a){jr(b.b,a);oc(b);}
function sc(a,b){return eo(a-b)>=100;}
function vb(){}
_=vb.prototype=new ko();_.tI=0;_.c=false;_.e=false;function pe(){pe=yt;xe=ir(new gr());{we();}}
function ne(a){pe();return a;}
function oe(a){if(a.b){se(a.c);}else{te(a.c);}rr(xe,a);}
function qe(a){if(!a.b){rr(xe,a);}a.bb();}
function re(b,a){if(a<=0){throw zn(new yn(),'must be positive');}oe(b);b.b=false;b.c=ue(b,a);jr(xe,b);}
function se(a){pe();$wnd.clearInterval(a);}
function te(a){pe();$wnd.clearTimeout(a);}
function ue(b,a){pe();return $wnd.setTimeout(function(){b.q();},a);}
function ve(){var a;a=o;{qe(this);}}
function we(){pe();Ce(new je());}
function ie(){}
_=ie.prototype=new ko();_.q=ve;_.tI=9;_.b=false;_.c=0;var xe;function yb(){yb=yt;pe();}
function xb(b,a){yb();b.a=a;ne(b);return b;}
function zb(){if(!this.a.c){return;}mc(this.a);}
function wb(){}
_=wb.prototype=new ie();_.bb=zb;_.tI=10;function Cb(){Cb=yt;pe();}
function Bb(b,a){Cb();b.a=a;ne(b);return b;}
function Db(){qc(this.a,false);nc(this.a,Co());}
function Ab(){}
_=Ab.prototype=new ie();_.bb=Db;_.tI=11;function Fb(b,a){b.d=a;return b;}
function bc(a){return mr(a.d.b,a.b);}
function cc(a){return a.c<a.a;}
function dc(b){var a;b.b=b.c;a=mr(b.d.b,b.c++);if(b.c>=b.a){b.c=0;}return a;}
function ec(a){qr(a.d.b,a.b);--a.a;if(a.b<=a.c){if(--a.c<0){a.c=0;}}a.b=(-1);}
function fc(b,a){b.a=a;}
function gc(a){return a.b==(-1);}
function hc(){return cc(this);}
function ic(){return dc(this);}
function Eb(){}
_=Eb.prototype=new ko();_.v=hc;_.y=ic;_.tI=0;_.a=0;_.b=(-1);_.c=0;function vc(){vc=yt;qd=ir(new gr());{kd=new kf();vf(kd);}}
function wc(b,a){vc();yf(kd,b,a);}
function xc(a,b){vc();return qf(kd,a,b);}
function yc(){vc();return Af(kd,'A');}
function zc(){vc();return Af(kd,'div');}
function Ac(a){vc();return Af(kd,a);}
function Bc(){vc();return Af(kd,'img');}
function Cc(){vc();return Bf(kd,'text');}
function Dc(){vc();return Af(kd,'tbody');}
function Ec(){vc();return Af(kd,'tr');}
function Fc(){vc();return Af(kd,'table');}
function cd(b,a,d){vc();var c;c=o;{bd(b,a,d);}}
function bd(b,a,c){vc();var d;if(a===pd){if(ed(b)==8192){pd=null;}}d=ad;ad=b;try{c.z(b);}finally{ad=d;}}
function dd(b,a){vc();Cf(kd,b,a);}
function ed(a){vc();return Df(kd,a);}
function fd(a){vc();rf(kd,a);}
function gd(b,a){vc();return sf(kd,b,a);}
function hd(a){vc();return Ef(kd,a);}
function id(a){vc();return tf(kd,a);}
function jd(a){vc();return uf(kd,a);}
function ld(c,a,b){vc();wf(kd,c,a,b);}
function md(a){vc();var b,c;c=true;if(qd.b>0){b=mb(mr(qd,qd.b-1));if(!(c=null.fb())){dd(a,true);fd(a);}}return c;}
function nd(b,a){vc();Ff(kd,b,a);}
function od(b,a){vc();ag(kd,b,a);}
function rd(b,a,c){vc();bg(kd,b,a,c);}
function td(a,b,c){vc();dg(kd,a,b,c);}
function sd(a,b,c){vc();cg(kd,a,b,c);}
function ud(a,b){vc();eg(kd,a,b);}
function vd(a,b){vc();fg(kd,a,b);}
function wd(a,b){vc();gg(kd,a,b);}
function xd(b,a,c){vc();hg(kd,b,a,c);}
function yd(a,b){vc();xf(kd,a,b);}
function zd(){vc();return mf(kd);}
function Ad(){vc();return nf(kd);}
var ad=null,kd=null,pd=null,qd;function Cd(){Cd=yt;Ed=kc(new vb());}
function Dd(a){Cd();if(a===null){throw io(new ho(),'cmd can not be null');}rc(Ed,a);}
var Ed;function be(a){if(lb(a,5)){return xc(this,kb(a,5));}return x(pb(this,Fd),a);}
function ce(){return y(pb(this,Fd));}
function Fd(){}
_=Fd.prototype=new v();_.eQ=be;_.hC=ce;_.tI=12;function ge(a){return x(pb(this,de),a);}
function he(){return y(pb(this,de));}
function de(){}
_=de.prototype=new v();_.eQ=ge;_.hC=he;_.tI=13;function le(){while((pe(),xe).b>0){oe(kb(mr((pe(),xe),0),6));}}
function me(){return null;}
function je(){}
_=je.prototype=new ko();_.C=le;_.D=me;_.tI=14;function Be(){Be=yt;De=ir(new gr());hf=ir(new gr());{df();}}
function Ce(a){Be();jr(De,a);}
function Ee(){Be();var a,b;for(a=up(De);np(a);){b=kb(op(a),7);b.C();}}
function Fe(){Be();var a,b,c,d;d=null;for(a=up(De);np(a);){b=kb(op(a),7);c=b.D();{d=c;}}return d;}
function af(){Be();var a,b;for(a=up(hf);np(a);){b=kb(op(a),8);b.E(cf(),bf());}}
function bf(){Be();return zd();}
function cf(){Be();return Ad();}
function df(){Be();__gwt_initHandlers(function(){gf();},function(){return ff();},function(){ef();$wnd.onresize=null;$wnd.onbeforeclose=null;$wnd.onclose=null;});}
function ef(){Be();var a;a=o;{Ee();}}
function ff(){Be();var a;a=o;{return Fe();}}
function gf(){Be();var a;a=o;{af();}}
var De,hf;function yf(c,b,a){b.appendChild(a);}
function Af(b,a){return $doc.createElement(a);}
function Bf(b,c){var a=$doc.createElement('INPUT');a.type=c;return a;}
function Cf(c,b,a){b.cancelBubble=a;}
function Df(b,a){switch(a.type){case 'blur':return 4096;case 'change':return 1024;case 'click':return 1;case 'dblclick':return 2;case 'focus':return 2048;case 'keydown':return 128;case 'keypress':return 256;case 'keyup':return 512;case 'load':return 32768;case 'losecapture':return 8192;case 'mousedown':return 4;case 'mousemove':return 64;case 'mouseout':return 32;case 'mouseover':return 16;case 'mouseup':return 8;case 'scroll':return 16384;case 'error':return 65536;case 'mousewheel':return 131072;case 'DOMMouseScroll':return 131072;}}
function Ef(b,a){return a.__eventBits||0;}
function Ff(c,b,a){b.removeChild(a);}
function ag(c,b,a){b.removeAttribute(a);}
function bg(c,b,a,d){b.setAttribute(a,d);}
function dg(c,a,b,d){a[b]=d;}
function cg(c,a,b,d){a[b]=d;}
function eg(c,a,b){a.__listener=b;}
function fg(c,a,b){a.src=b;}
function gg(c,a,b){if(!b){b='';}a.innerHTML=b;}
function hg(c,b,a,d){b.style[a]=d;}
function jf(){}
_=jf.prototype=new ko();_.tI=0;function qf(c,a,b){return a==b;}
function rf(b,a){a.preventDefault();}
function sf(f,c,d){var b=0,a=c.firstChild;while(a){var e=a.nextSibling;if(a.nodeType==1){if(d==b)return a;++b;}a=e;}return null;}
function tf(c,b){var a=b.firstChild;while(a&&a.nodeType!=1)a=a.nextSibling;return a||null;}
function uf(c,a){var b=a.parentNode;if(b==null){return null;}if(b.nodeType!=1)b=null;return b||null;}
function vf(d){$wnd.__dispatchCapturedMouseEvent=function(b){if($wnd.__dispatchCapturedEvent(b)){var a=$wnd.__captureElem;if(a&&a.__listener){cd(b,a,a.__listener);b.stopPropagation();}}};$wnd.__dispatchCapturedEvent=function(a){if(!md(a)){a.stopPropagation();a.preventDefault();return false;}return true;};$wnd.addEventListener('click',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('dblclick',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mousedown',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mouseup',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mousemove',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mousewheel',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('keydown',$wnd.__dispatchCapturedEvent,true);$wnd.addEventListener('keyup',$wnd.__dispatchCapturedEvent,true);$wnd.addEventListener('keypress',$wnd.__dispatchCapturedEvent,true);$wnd.__dispatchEvent=function(b){var c,a=this;while(a&& !(c=a.__listener))a=a.parentNode;if(a&&a.nodeType!=1)a=null;if(c)cd(b,a,c);};$wnd.__captureElem=null;}
function wf(f,e,g,d){var c=0,b=e.firstChild,a=null;while(b){if(b.nodeType==1){if(c==d){a=b;break;}++c;}b=b.nextSibling;}e.insertBefore(g,a);}
function xf(c,b,a){b.__eventBits=a;b.onclick=a&1?$wnd.__dispatchEvent:null;b.ondblclick=a&2?$wnd.__dispatchEvent:null;b.onmousedown=a&4?$wnd.__dispatchEvent:null;b.onmouseup=a&8?$wnd.__dispatchEvent:null;b.onmouseover=a&16?$wnd.__dispatchEvent:null;b.onmouseout=a&32?$wnd.__dispatchEvent:null;b.onmousemove=a&64?$wnd.__dispatchEvent:null;b.onkeydown=a&128?$wnd.__dispatchEvent:null;b.onkeypress=a&256?$wnd.__dispatchEvent:null;b.onkeyup=a&512?$wnd.__dispatchEvent:null;b.onchange=a&1024?$wnd.__dispatchEvent:null;b.onfocus=a&2048?$wnd.__dispatchEvent:null;b.onblur=a&4096?$wnd.__dispatchEvent:null;b.onlosecapture=a&8192?$wnd.__dispatchEvent:null;b.onscroll=a&16384?$wnd.__dispatchEvent:null;b.onload=a&32768?$wnd.__dispatchEvent:null;b.onerror=a&65536?$wnd.__dispatchEvent:null;b.onmousewheel=a&131072?$wnd.__dispatchEvent:null;}
function of(){}
_=of.prototype=new jf();_.tI=0;function mf(a){return $wnd.innerHeight;}
function nf(a){return $wnd.innerWidth;}
function kf(){}
_=kf.prototype=new of();_.tI=0;function gl(d,b,a){var c=b.parentNode;if(!c){return;}c.insertBefore(a,b);c.removeChild(b);}
function hl(b,a){if(b.h!==null){gl(b,b.h,a);}b.h=a;}
function il(b,a){xd(b.h,'height',a);}
function jl(b,c,a){nl(b,c);il(b,a);}
function kl(b,a){pl(b.h,a);}
function ll(b,a){ql(b.h,a);}
function ml(a,b){if(b===null||to(b)==0){od(a.h,'title');}else{rd(a.h,'title',b);}}
function nl(a,b){xd(a.h,'width',b);}
function ol(b,a){yd(b.h,a|hd(b.h));}
function pl(a,b){td(a,'className',b);}
function ql(a,b){if(a===null){throw po(new oo(),'Null widget handle. If you are creating a composite, ensure that initWidget() has been called.');}b=vo(b);if(to(b)==0){throw zn(new yn(),'Style names cannot be empty');}rl(a,b);}
function rl(b,f){var a=b.className.split(/\s+/);if(!a){return;}var g=a[0];var h=g.length;a[0]=f;for(var c=1,d=a.length;c<d;c++){var e=a[c];if(e.length>h&&(e.charAt(h)=='-'&&e.indexOf(g)==0)){a[c]=f+e.substring(h);}}b.className=a.join(' ');}
function el(){}
_=el.prototype=new ko();_.tI=0;_.h=null;function cm(a){if(a.f){throw Cn(new Bn(),"Should only call onAttach when the widget is detached from the browser's document");}a.f=true;ud(a.h,a);a.m();a.A();}
function dm(a){if(!a.f){throw Cn(new Bn(),"Should only call onDetach when the widget is attached to the browser's document");}try{a.B();}finally{a.n();ud(a.h,null);a.f=false;}}
function em(a){if(a.g!==null){a.g.ab(a);}else if(a.g!==null){throw Cn(new Bn(),"This widget's parent does not implement HasWidgets");}}
function fm(b,a){if(b.f){ud(b.h,null);}hl(b,a);if(b.f){ud(a,b);}}
function gm(c,b){var a;a=c.g;if(b===null){if(a!==null&&a.f){dm(c);}c.g=null;}else{if(a!==null){throw Cn(new Bn(),'Cannot set a new parent without first clearing the old parent');}c.g=b;if(b.f){cm(c);}}}
function hm(){}
function im(){}
function jm(a){}
function km(){}
function lm(){}
function mm(a){fm(this,a);}
function sl(){}
_=sl.prototype=new el();_.m=hm;_.n=im;_.z=jm;_.A=km;_.B=lm;_.cb=mm;_.tI=15;_.f=false;_.g=null;function Cj(b,a){gm(a,b);}
function Ej(b,a){gm(a,null);}
function Fj(){var a,b;for(b=this.w();b.v();){a=kb(b.y(),9);cm(a);}}
function ak(){var a,b;for(b=this.w();b.v();){a=kb(b.y(),9);dm(a);}}
function bk(){}
function ck(){}
function Bj(){}
_=Bj.prototype=new sl();_.m=Fj;_.n=ak;_.A=bk;_.B=ck;_.tI=16;function rg(a){a.a=zl(new tl(),a);}
function sg(a){rg(a);return a;}
function tg(c,a,b){em(a);Al(c.a,a);wc(b,a.h);Cj(c,a);}
function vg(b,c){var a;if(c.g!==b){return false;}Ej(b,c);a=c.h;nd(jd(a),a);am(b.a,c);return true;}
function wg(){return El(this.a);}
function xg(a){return vg(this,a);}
function qg(){}
_=qg.prototype=new Bj();_.w=wg;_.ab=xg;_.tI=17;function jg(a){sg(a);a.cb(zc());xd(a.h,'position','relative');xd(a.h,'overflow','hidden');return a;}
function kg(a,b){tg(a,b,a.h);}
function lg(b,d,a,c){em(d);ng(b,d,a,c);kg(b,d);}
function ng(c,e,b,d){var a;a=e.h;if(b==(-1)&&d==(-1)){og(a);}else{xd(a,'position','absolute');xd(a,'left',b+'px');xd(a,'top',d+'px');}}
function og(a){xd(a,'left','');xd(a,'top','');xd(a,'position','');}
function pg(b){var a;a=vg(this,b);if(a){og(b.h);}return a;}
function ig(){}
_=ig.prototype=new qg();_.ab=pg;_.tI=18;function qi(a){a.e=gi(new bi());}
function ri(a){qi(a);a.d=Fc();a.a=Dc();wc(a.d,a.a);a.cb(a.d);ol(a,1);return a;}
function si(c,a){var b;b=ah(c);if(a>=b||a<0){throw Fn(new En(),'Row index: '+a+', Row size: '+b);}}
function ti(e,c,b,a){var d;d=Ah(e.b,c,b);zi(e,d,a);return d;}
function vi(c,b,a){return b.rows[a].cells.length;}
function wi(a){return xi(a,a.a);}
function xi(b,a){return a.rows.length;}
function yi(b,a){var c;if(a!=ah(b)){si(b,a);}c=Ec();ld(b.a,c,a);return a;}
function zi(d,c,a){var b,e;b=id(c);e=null;if(b!==null){e=ii(d.e,b);}if(e!==null){Ai(d,e);return true;}else{if(a){wd(c,'');}return false;}}
function Ai(b,c){var a;if(c.g!==b){return false;}Ej(b,c);a=c.h;nd(jd(a),a);li(b.e,a);return true;}
function Bi(a,b){td(a.d,'border',''+b);}
function Ci(b,a){b.b=a;}
function Di(b,a){sd(b.d,'cellPadding',a);}
function Ei(b,a){sd(b.d,'cellSpacing',a);}
function Fi(b,a){b.c=a;ai(b.c);}
function aj(d,b,a,e){var c;ch(d,b,a);if(e!==null){em(e);c=ti(d,b,a,true);ji(d.e,e);wc(c,e.h);Cj(d,e);}}
function bj(){return mi(this.e);}
function cj(a){switch(ed(a)){case 1:{break;}default:}}
function dj(a){return Ai(this,a);}
function mh(){}
_=mh.prototype=new Bj();_.w=bj;_.z=cj;_.ab=dj;_.tI=19;_.a=null;_.b=null;_.c=null;_.d=null;function Dg(a){ri(a);Ci(a,Ag(new zg(),a));Fi(a,Eh(new Dh(),a));return a;}
function Fg(b,a){si(b,a);return vi(b,b.a,a);}
function ah(a){return wi(a);}
function bh(b,a){return yi(b,a);}
function ch(e,d,b){var a,c;dh(e,d);if(b<0){throw Fn(new En(),'Cannot create a column with a negative index: '+b);}a=Fg(e,d);c=b+1-a;if(c>0){eh(e.a,d,c);}}
function dh(d,b){var a,c;if(b<0){throw Fn(new En(),'Cannot create a row with a negative index: '+b);}c=ah(d);for(a=c;a<=b;a++){bh(d,a);}}
function eh(f,d,c){var e=f.rows[d];for(var b=0;b<c;b++){var a=$doc.createElement('td');e.appendChild(a);}}
function yg(){}
_=yg.prototype=new mh();_.tI=20;function wh(b,a){b.a=a;return b;}
function yh(c,b,a){ch(c.a,b,a);return zh(c,c.a.a,b,a);}
function zh(e,d,c,a){var b=d.rows[c].cells[a];return b==null?null:b;}
function Ah(c,b,a){return zh(c,c.a.a,b,a);}
function Bh(e,d,b,a){var c;ch(e.a,d,b);c=zh(e,e.a.a,d,b);td(c,'align',a.a);}
function Ch(c,b,a,d){ch(c.a,b,a);td(zh(c,c.a.a,b,a),'width',d);}
function vh(){}
_=vh.prototype=new ko();_.tI=0;function Ag(b,a){wh(b,a);return b;}
function Cg(d,c,b,a){sd(yh(d,c,b),'colSpan',a);}
function zg(){}
_=zg.prototype=new vh();_.tI=0;function hh(){hh=yt;zm(),Bm;}
function gh(b,a){zm(),Bm;jh(b,a);return b;}
function ih(b,a){switch(ed(a)){case 1:break;case 4096:case 2048:break;case 128:case 512:case 256:break;}}
function jh(b,a){fm(b,a);ol(b,7041);}
function kh(a){ih(this,a);}
function lh(a){jh(this,a);}
function fh(){}
_=fh.prototype=new sl();_.z=kh;_.cb=lh;_.tI=21;function oh(a){{rh(a);}}
function ph(b,a){b.b=a;oh(b);return b;}
function rh(a){while(++a.a<a.b.b.b){if(mr(a.b.b,a.a)!==null){return;}}}
function sh(a){return a.a<a.b.b.b;}
function th(){return sh(this);}
function uh(){var a;if(!sh(this)){throw new ut();}a=mr(this.b.b,this.a);rh(this);return a;}
function nh(){}
_=nh.prototype=new ko();_.v=th;_.y=uh;_.tI=0;_.a=(-1);function Eh(b,a){b.b=a;return b;}
function ai(a){if(a.a===null){a.a=Ac('colgroup');ld(a.b.d,a.a,0);wc(a.a,Ac('col'));}}
function Dh(){}
_=Dh.prototype=new ko();_.tI=0;_.a=null;function fi(a){a.b=ir(new gr());}
function gi(a){fi(a);return a;}
function ii(c,a){var b;b=oi(a);if(b<0){return null;}return kb(mr(c.b,b),9);}
function ji(b,c){var a;if(b.a===null){a=b.b.b;jr(b.b,c);}else{a=b.a.a;sr(b.b,a,c);b.a=b.a.b;}pi(c.h,a);}
function ki(c,a,b){ni(a);sr(c.b,b,null);c.a=di(new ci(),b,c.a);}
function li(c,a){var b;b=oi(a);ki(c,a,b);}
function mi(a){return ph(new nh(),a);}
function ni(a){a['__widgetID']=null;}
function oi(a){var b=a['__widgetID'];return b==null?-1:b;}
function pi(a,b){a['__widgetID']=b;}
function bi(){}
_=bi.prototype=new ko();_.tI=0;_.a=null;function di(c,a,b){c.a=a;c.b=b;return c;}
function ci(){}
_=ci.prototype=new ko();_.tI=0;_.a=0;_.b=null;function jj(){jj=yt;kj=hj(new gj(),'center');hj(new gj(),'left');hj(new gj(),'right');}
var kj;function hj(b,a){b.a=a;return b;}
function gj(){}
_=gj.prototype=new ko();_.tI=0;_.a=null;function xj(){xj=yt;zs(new as());}
function vj(a){xj();wj(a,sj(new rj(),a));kl(a,'gwt-Image');return a;}
function wj(b,a){b.a=a;}
function yj(a,b){uj(a.a,a,b);}
function zj(a){switch(ed(a)){case 1:{break;}case 4:case 8:case 64:case 16:case 32:{break;}case 131072:break;case 32768:{break;}case 65536:{break;}}}
function oj(){}
_=oj.prototype=new sl();_.z=zj;_.tI=22;_.a=null;function pj(){}
_=pj.prototype=new ko();_.tI=0;function sj(b,a){a.cb(Bc());ol(a,229501);return b;}
function uj(b,a,c){vd(a.h,c);}
function rj(){}
_=rj.prototype=new pj();_.tI=0;function jk(){jk=yt;ok=zs(new as());}
function ik(b,a){jk();jg(b);if(a===null){a=kk();}b.cb(a);cm(b);return b;}
function lk(){jk();return mk(null);}
function mk(c){jk();var a,b;b=kb(Fs(ok,c),10);if(b!==null){return b;}a=null;if(ok.c==0){nk();}at(ok,c,b=ik(new dk(),a));return b;}
function kk(){jk();return $doc.body;}
function nk(){jk();Ce(new ek());}
function dk(){}
_=dk.prototype=new ig();_.tI=23;var ok;function gk(){var a,b;for(b=nq(Bq((jk(),ok)));uq(b);){a=kb(vq(b),10);if(a.f){dm(a);}}}
function hk(){return null;}
function ek(){}
_=ek.prototype=new ko();_.C=gk;_.D=hk;_.tI=24;function Dk(){Dk=yt;zm(),Bm;al=Ak(new zk(),'center');Ak(new zk(),'justify');Ak(new zk(),'left');Ak(new zk(),'right');}
function Ck(b,a){Dk();gh(b,a);ol(b,1024);return b;}
function Fk(b,a){td(b.h,'value',a!==null?a:'');}
function Ek(b,a){xd(b.h,'textAlign',a.a);}
function bl(a){var b;ih(this,a);b=ed(a);}
function yk(){}
_=yk.prototype=new fh();_.z=bl;_.tI=25;var al;function dl(){dl=yt;Dk();}
function cl(a){dl();Ck(a,Cc());kl(a,'gwt-TextBox');return a;}
function xk(){}
_=xk.prototype=new yk();_.tI=26;function Ak(b,a){b.a=a;return b;}
function zk(){}
_=zk.prototype=new ko();_.tI=0;_.a=null;function zl(b,a){b.a=fb('[Lcom.google.gwt.user.client.ui.Widget;',[0],[9],[4],null);return b;}
function Al(a,b){Dl(a,b,a.b);}
function Cl(b,c){var a;for(a=0;a<b.b;++a){if(b.a[a]===c){return a;}}return (-1);}
function Dl(d,e,a){var b,c;if(a<0||a>d.b){throw new En();}if(d.b==d.a.a){c=fb('[Lcom.google.gwt.user.client.ui.Widget;',[0],[9],[d.a.a*2],null);for(b=0;b<d.a.a;++b){gb(c,b,d.a[b]);}d.a=c;}++d.b;for(b=d.b-1;b>a;--b){gb(d.a,b,d.a[b-1]);}gb(d.a,a,e);}
function El(a){return vl(new ul(),a);}
function Fl(c,b){var a;if(b<0||b>=c.b){throw new En();}--c.b;for(a=b;a<c.b;++a){gb(c.a,a,c.a[a+1]);}gb(c.a,c.b,null);}
function am(b,c){var a;a=Cl(b,c);if(a==(-1)){throw new ut();}Fl(b,a);}
function tl(){}
_=tl.prototype=new ko();_.tI=0;_.a=null;_.b=0;function vl(b,a){b.b=a;return b;}
function xl(){return this.a<this.b.b-1;}
function yl(){if(this.a>=this.b.b){throw new ut();}return this.b.a[++this.a];}
function ul(){}
_=ul.prototype=new ko();_.v=xl;_.y=yl;_.tI=0;_.a=(-1);function zm(){zm=yt;Am=vm(new um());Bm=Am!==null?ym(new nm()):Am;}
function ym(a){zm();return a;}
function nm(){}
_=nm.prototype=new ko();_.tI=0;var Am,Bm;function rm(){rm=yt;zm();}
function pm(a){sm(a);tm(a);xm(a);}
function qm(a){rm();ym(a);pm(a);return a;}
function sm(b){return function(a){if(this.parentNode.onblur){this.parentNode.onblur(a);}};}
function tm(b){return function(a){if(this.parentNode.onfocus){this.parentNode.onfocus(a);}};}
function om(){}
_=om.prototype=new nm();_.tI=0;function wm(){wm=yt;rm();}
function vm(a){wm();qm(a);return a;}
function xm(b){return function(){var a=this.firstChild;$wnd.setTimeout(function(){a.focus();},0);};}
function um(){}
_=um.prototype=new om();_.tI=0;function Dm(a){a.cb(yc());return a;}
function Fm(b,a){rd(b.h,'href',a===null?'':a);}
function an(b,a){rd(b.h,'id',a===null?'':a);}
function bn(c,d){var a,b;a=c.h;b=gd(a,0);if(b===null){b=Bc();ld(a,b,0);}vd(b,d);}
function cn(b,a){rd(b.h,'target',a===null?'':a);}
function Cm(){}
_=Cm.prototype=new sl();_.tI=27;function hn(a){a.f=Dg(new yg());a.b=Dm(new Cm());a.a=Dm(new Cm());a.d=Dm(new Cm());a.c=Dm(new Cm());a.e=cl(new xk());}
function kn(a){hn(a);return a;}
function ln(e){var a,b,c,d;lk();d=lk();jl(d,'100%','100%');ll(d,'rootPanel');kl(d,'rootPanel');lg(d,e.f,60,0);Bi(e.f,2);jl(e.f,'377px','270px');Ei(e.f,5);Di(e.f,5);aj(e.f,1,0,e.b);Bh(e.f.b,1,0,(jj(),kj));cn(e.b,'_blank');Fm(e.b,'http://www.linkedin.com/in/JeanLouDupont');an(e.b,'link_linkedin');bn(e.b,'linkedin.gif');aj(e.f,1,1,e.a);Bh(e.f.b,1,1,(jj(),kj));cn(e.a,'_blank');Fm(e.a,'http://jldupont.blogspot.com');an(e.a,'link_blog');bn(e.a,'blog.jpg');aj(e.f,2,0,e.d);Bh(e.f.b,2,0,(jj(),kj));cn(e.d,'_blank');Fm(e.d,'http://wiki.jldupont.com');an(e.d,'link_wiki');bn(e.d,'wiki.png');aj(e.f,2,1,e.c);Bh(e.f.b,2,1,(jj(),kj));cn(e.c,'_blank');Fm(e.c,'http://code.google.com/u/JeanLou.Dupont/');an(e.c,'link_projects');bn(e.c,'projects.jpg');aj(e.f,0,0,e.e);kl(e.e,'title');Ek(e.e,(Dk(),al));ml(e.e,'title');Bh(e.f.b,0,0,(jj(),kj));Fk(e.e,"Jean-Lou Dupont's WEB site");Cg(e.f.b,0,0,2);nl(e.e,'100%');c=Dg(new yg());lg(d,c,330,367);jl(c,'107px','40px');b=vj(new oj());aj(c,0,0,b);Ch(c.b,0,0,'43px');yj(b,'gwt.png');a=vj(new oj());aj(c,0,1,a);Ch(c.b,0,1,'50px');yj(a,'gae.png');Dd(new en());cf(),bf();}
function mn(b,a){}
function dn(){}
_=dn.prototype=new ko();_.E=mn;_.tI=28;function gn(){cf(),bf();}
function en(){}
_=en.prototype=new ko();_.p=gn;_.tI=29;function on(){}
_=on.prototype=new oo();_.tI=30;function rn(){}
_=rn.prototype=new oo();_.tI=31;function zn(b,a){po(b,a);return b;}
function yn(){}
_=yn.prototype=new oo();_.tI=32;function Cn(b,a){po(b,a);return b;}
function Bn(){}
_=Bn.prototype=new oo();_.tI=33;function Fn(b,a){po(b,a);return b;}
function En(){}
_=En.prototype=new oo();_.tI=34;function eo(a){return a<0?-a:a;}
function fo(){}
_=fo.prototype=new oo();_.tI=35;function io(b,a){po(b,a);return b;}
function ho(){}
_=ho.prototype=new oo();_.tI=36;function to(a){return a.length;}
function uo(b,a){return b.substr(a,b.length-a);}
function vo(c){var a=c.replace(/^(\s*)/,'');var b=a.replace(/\s*$/,'');return b;}
function wo(a,b){return String(a)==b;}
function xo(a){if(!lb(a,1))return false;return wo(this,a);}
function zo(){var a=yo;if(!a){a=yo={};}var e=':'+this;var b=a[e];if(b==null){b=0;var f=this.length;var d=f<64?1:f/32|0;for(var c=0;c<f;c+=d){b<<=1;b+=this.charCodeAt(c);}b|=0;a[e]=b;}return b;}
_=String.prototype;_.eQ=xo;_.hC=zo;_.tI=2;var yo=null;function Co(){return new Date().getTime();}
function Do(a){return s(a);}
function cp(b,a){po(b,a);return b;}
function bp(){}
_=bp.prototype=new oo();_.tI=37;function fp(d,a,b){var c;while(a.v()){c=a.y();if(b===null?c===null:b.eQ(c)){return a;}}return null;}
function hp(a){throw cp(new bp(),'add');}
function ip(b){var a;a=fp(this,this.w(),b);return a!==null;}
function ep(){}
_=ep.prototype=new ko();_.j=hp;_.l=ip;_.tI=0;function tp(b,a){throw Fn(new En(),'Index: '+a+', Size: '+b.b);}
function up(a){return lp(new kp(),a);}
function vp(b,a){throw cp(new bp(),'add');}
function wp(a){this.i(this.db(),a);return true;}
function xp(e){var a,b,c,d,f;if(e===this){return true;}if(!lb(e,14)){return false;}f=kb(e,14);if(this.db()!=f.db()){return false;}c=up(this);d=f.w();while(np(c)){a=op(c);b=op(d);if(!(a===null?b===null:a.eQ(b))){return false;}}return true;}
function yp(){var a,b,c,d;c=1;a=31;b=up(this);while(np(b)){d=op(b);c=31*c+(d===null?0:d.hC());}return c;}
function zp(){return up(this);}
function Ap(a){throw cp(new bp(),'remove');}
function jp(){}
_=jp.prototype=new ep();_.i=vp;_.j=wp;_.eQ=xp;_.hC=yp;_.w=zp;_.F=Ap;_.tI=38;function lp(b,a){b.c=a;return b;}
function np(a){return a.a<a.c.db();}
function op(a){if(!np(a)){throw new ut();}return a.c.t(a.b=a.a++);}
function pp(a){if(a.b<0){throw new Bn();}a.c.F(a.b);a.a=a.b;a.b=(-1);}
function qp(){return np(this);}
function rp(){return op(this);}
function kp(){}
_=kp.prototype=new ko();_.v=qp;_.y=rp;_.tI=0;_.a=0;_.b=(-1);function zq(f,d,e){var a,b,c;for(b=us(f.o());ns(b);){a=os(b);c=a.r();if(d===null?c===null:d.eQ(c)){if(e){ps(b);}return a;}}return null;}
function Aq(b){var a;a=b.o();return Dp(new Cp(),b,a);}
function Bq(b){var a;a=Es(b);return lq(new kq(),b,a);}
function Cq(a){return zq(this,a,false)!==null;}
function Dq(d){var a,b,c,e,f,g,h;if(d===this){return true;}if(!lb(d,15)){return false;}f=kb(d,15);c=Aq(this);e=f.x();if(!dr(c,e)){return false;}for(a=Fp(c);gq(a);){b=hq(a);h=this.u(b);g=f.u(b);if(h===null?g!==null:!h.eQ(g)){return false;}}return true;}
function Eq(b){var a;a=zq(this,b,false);return a===null?null:a.s();}
function Fq(){var a,b,c;b=0;for(c=us(this.o());ns(c);){a=os(c);b+=a.hC();}return b;}
function ar(){return Aq(this);}
function Bp(){}
_=Bp.prototype=new ko();_.k=Cq;_.eQ=Dq;_.u=Eq;_.hC=Fq;_.x=ar;_.tI=39;function dr(e,b){var a,c,d;if(b===e){return true;}if(!lb(b,16)){return false;}c=kb(b,16);if(c.db()!=e.db()){return false;}for(a=c.w();a.v();){d=a.y();if(!e.l(d)){return false;}}return true;}
function er(a){return dr(this,a);}
function fr(){var a,b,c;a=0;for(b=this.w();b.v();){c=b.y();if(c!==null){a+=c.hC();}}return a;}
function br(){}
_=br.prototype=new ep();_.eQ=er;_.hC=fr;_.tI=40;function Dp(b,a,c){b.a=a;b.b=c;return b;}
function Fp(b){var a;a=us(b.b);return eq(new dq(),b,a);}
function aq(a){return this.a.k(a);}
function bq(){return Fp(this);}
function cq(){return this.b.a.c;}
function Cp(){}
_=Cp.prototype=new br();_.l=aq;_.w=bq;_.db=cq;_.tI=41;function eq(b,a,c){b.a=c;return b;}
function gq(a){return a.a.v();}
function hq(b){var a;a=b.a.y();return a.r();}
function iq(){return gq(this);}
function jq(){return hq(this);}
function dq(){}
_=dq.prototype=new ko();_.v=iq;_.y=jq;_.tI=0;function lq(b,a,c){b.a=a;b.b=c;return b;}
function nq(b){var a;a=us(b.b);return sq(new rq(),b,a);}
function oq(a){return Ds(this.a,a);}
function pq(){return nq(this);}
function qq(){return this.b.a.c;}
function kq(){}
_=kq.prototype=new ep();_.l=oq;_.w=pq;_.db=qq;_.tI=0;function sq(b,a,c){b.a=c;return b;}
function uq(a){return a.a.v();}
function vq(a){var b;b=a.a.y().s();return b;}
function wq(){return uq(this);}
function xq(){return vq(this);}
function rq(){}
_=rq.prototype=new ko();_.v=wq;_.y=xq;_.tI=0;function hr(a){{kr(a);}}
function ir(a){hr(a);return a;}
function jr(b,a){Cr(b.a,b.b++,a);return true;}
function kr(a){a.a=z();a.b=0;}
function mr(b,a){if(a<0||a>=b.b){tp(b,a);}return yr(b.a,a);}
function nr(b,a){return or(b,a,0);}
function or(c,b,a){if(a<0){tp(c,a);}for(;a<c.b;++a){if(xr(b,yr(c.a,a))){return a;}}return (-1);}
function pr(a){return a.b==0;}
function qr(c,a){var b;b=mr(c,a);Ar(c.a,a,1);--c.b;return b;}
function rr(c,b){var a;a=nr(c,b);if(a==(-1)){return false;}qr(c,a);return true;}
function sr(d,a,b){var c;c=mr(d,a);Cr(d.a,a,b);return c;}
function ur(a,b){if(a<0||a>this.b){tp(this,a);}tr(this.a,a,b);++this.b;}
function vr(a){return jr(this,a);}
function tr(a,b,c){a.splice(b,0,c);}
function wr(a){return nr(this,a)!=(-1);}
function xr(a,b){return a===b||a!==null&&a.eQ(b);}
function zr(a){return mr(this,a);}
function yr(a,b){return a[b];}
function Br(a){return qr(this,a);}
function Ar(a,c,b){a.splice(c,b);}
function Cr(a,b,c){a[b]=c;}
function Dr(){return this.b;}
function gr(){}
_=gr.prototype=new jp();_.i=ur;_.j=vr;_.l=wr;_.t=zr;_.F=Br;_.db=Dr;_.tI=42;_.a=null;_.b=0;function Bs(){Bs=yt;ct=it();}
function ys(a){{As(a);}}
function zs(a){Bs();ys(a);return a;}
function As(a){a.a=z();a.d=A();a.b=pb(ct,v);a.c=0;}
function Cs(b,a){if(lb(a,1)){return mt(b.d,kb(a,1))!==ct;}else if(a===null){return b.b!==ct;}else{return lt(b.a,a,a.hC())!==ct;}}
function Ds(a,b){if(a.b!==ct&&kt(a.b,b)){return true;}else if(ht(a.d,b)){return true;}else if(ft(a.a,b)){return true;}return false;}
function Es(a){return ss(new js(),a);}
function Fs(c,a){var b;if(lb(a,1)){b=mt(c.d,kb(a,1));}else if(a===null){b=c.b;}else{b=lt(c.a,a,a.hC());}return b===ct?null:b;}
function at(c,a,d){var b;{b=c.b;c.b=d;}if(b===ct){++c.c;return null;}else{return b;}}
function bt(c,a){var b;if(lb(a,1)){b=pt(c.d,kb(a,1));}else if(a===null){b=c.b;c.b=pb(ct,v);}else{b=ot(c.a,a,a.hC());}if(b===ct){return null;}else{--c.c;return b;}}
function dt(e,c){Bs();for(var d in e){if(d==parseInt(d)){var a=e[d];for(var f=0,b=a.length;f<b;++f){c.j(a[f]);}}}}
function et(d,a){Bs();for(var c in d){if(c.charCodeAt(0)==58){var e=d[c];var b=es(c.substring(1),e);a.j(b);}}}
function ft(f,h){Bs();for(var e in f){if(e==parseInt(e)){var a=f[e];for(var g=0,b=a.length;g<b;++g){var c=a[g];var d=c.s();if(kt(h,d)){return true;}}}}return false;}
function gt(a){return Cs(this,a);}
function ht(c,d){Bs();for(var b in c){if(b.charCodeAt(0)==58){var a=c[b];if(kt(d,a)){return true;}}}return false;}
function it(){Bs();}
function jt(){return Es(this);}
function kt(a,b){Bs();if(a===b){return true;}else if(a===null){return false;}else{return a.eQ(b);}}
function nt(a){return Fs(this,a);}
function lt(f,h,e){Bs();var a=f[e];if(a){for(var g=0,b=a.length;g<b;++g){var c=a[g];var d=c.r();if(kt(h,d)){return c.s();}}}}
function mt(b,a){Bs();return b[':'+a];}
function ot(f,h,e){Bs();var a=f[e];if(a){for(var g=0,b=a.length;g<b;++g){var c=a[g];var d=c.r();if(kt(h,d)){if(a.length==1){delete f[e];}else{a.splice(g,1);}return c.s();}}}}
function pt(c,a){Bs();a=':'+a;var b=c[a];delete c[a];return b;}
function as(){}
_=as.prototype=new Bp();_.k=gt;_.o=jt;_.u=nt;_.tI=43;_.a=null;_.b=null;_.c=0;_.d=null;var ct;function cs(b,a,c){b.a=a;b.b=c;return b;}
function es(a,b){return cs(new bs(),a,b);}
function fs(b){var a;if(lb(b,17)){a=kb(b,17);if(kt(this.a,a.r())&&kt(this.b,a.s())){return true;}}return false;}
function gs(){return this.a;}
function hs(){return this.b;}
function is(){var a,b;a=0;b=0;if(this.a!==null){a=this.a.hC();}if(this.b!==null){b=this.b.hC();}return a^b;}
function bs(){}
_=bs.prototype=new ko();_.eQ=fs;_.r=gs;_.s=hs;_.hC=is;_.tI=44;_.a=null;_.b=null;function ss(b,a){b.a=a;return b;}
function us(a){return ls(new ks(),a.a);}
function vs(c){var a,b,d;if(lb(c,17)){a=kb(c,17);b=a.r();if(Cs(this.a,b)){d=Fs(this.a,b);return kt(a.s(),d);}}return false;}
function ws(){return us(this);}
function xs(){return this.a.c;}
function js(){}
_=js.prototype=new br();_.l=vs;_.w=ws;_.db=xs;_.tI=45;function ls(c,b){var a;c.c=b;a=ir(new gr());if(c.c.b!==(Bs(),ct)){jr(a,cs(new bs(),null,c.c.b));}et(c.c.d,a);dt(c.c.a,a);c.a=up(a);return c;}
function ns(a){return np(a.a);}
function os(a){return a.b=kb(op(a.a),17);}
function ps(a){if(a.b===null){throw Cn(new Bn(),'Must call next() before remove().');}else{pp(a.a);bt(a.c,a.b.r());a.b=null;}}
function qs(){return ns(this);}
function rs(){return os(this);}
function ks(){}
_=ks.prototype=new ko();_.v=qs;_.y=rs;_.tI=0;_.a=null;_.b=null;function ut(){}
_=ut.prototype=new oo();_.tI=46;function nn(){ln(kn(new dn()));Dm(new Cm());}
function gwtOnLoad(b,d,c){$moduleName=d;$moduleBase=c;if(b)try{nn();}catch(a){b(d);}else{nn();}}
var ob=[{},{},{1:1},{3:1},{3:1},{3:1},{3:1},{2:1},{3:1},{6:1},{6:1},{6:1},{2:1,5:1},{2:1},{7:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,10:1,11:1,12:1,13:1},{7:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{8:1},{4:1},{3:1},{3:1},{3:1},{3:1},{3:1},{3:1},{3:1},{3:1},{14:1},{15:1},{16:1},{16:1},{14:1},{15:1},{17:1},{16:1},{3:1}];if (com_jldupont_project_main) {  var __gwt_initHandlers = com_jldupont_project_main.__gwt_initHandlers;  com_jldupont_project_main.onScriptLoad(gwtOnLoad);}})();