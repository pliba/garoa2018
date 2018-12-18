(*****************************************************************
 *                     DECLARATIONS                              *
 *****************************************************************)

program chapter1 (input, output);

   (* ... *)

type

   (* ... *)
   BUILTINOP = (IFOP,WHILEOP,SETOP,BEGINOP,PLUSOP,MINUSOP,
             TIMESOP,DIVOP,EQOP,LTOP,GTOP,PRINTOP);
   VALUEOP = PLUSOP .. PRINTOP;
   CONTROLOP = IFOP .. BEGINOP;

   EXP = ^EXPREC;
   EXPLIST = ^EXPLISTREC;
   ENV = ^ENVREC;
   VALUELIST = ^VALUELISTREC;
   NAMELIST = ^NAMELISTREC;
   FUNDEF = ^FUNDEFREC;

   EXPTYPE = (VALEXP,VAREXP,APEXP);
   EXPREC = record
               case etype: EXPTYPE of
                  VALEXP: (num: NUMBER);
                  VAREXP: (varble: NAME);
                  APEXP: (optr: NAME; args: EXPLIST)
            end;

   EXPLISTREC = record
               head: EXP;
               tail: EXPLIST
            end;

   VALUELISTREC = record
               head: NUMBER;
               tail: VALUELIST
            end;

   NAMELISTREC = record
               head: NAME;
               tail: NAMELIST
            end;

   ENVREC = record
               vars: NAMELIST;
               values: VALUELIST
            end;

   FUNDEFREC = record
               funname: NAME;
               formals: NAMELIST;
               body: EXP;
               nextfundef: FUNDEF
            end;

var
   fundefs: FUNDEF;

   globalEnv: ENV;

   currentExp: EXP;

   userinput: array [1..MAXINPUT] of char;

   (* ... *)

(*****************************************************************
 *                     DATA STRUCTURE OP'S                       *
 *****************************************************************)

(* mkVALEXP - return an EXP of type VALEXP with num n            *)
function mkVALEXP (n: NUMBER): EXP;

(* mkVAREXP - return an EXP of type VAREXP with varble nm        *)
function mkVAREXP (nm: NAME): EXP;

(* mkAPEXP - return EXP of type APEXP w/ optr op and args el     *)
function mkAPEXP (op: NAME; el: EXPLIST): EXP;

(* mkExplist - return an EXPLIST with head e and tail el         *)
function mkExplist (e: EXP; el: EXPLIST): EXPLIST;

(* mkNamelist - return a NAMELIST with head n and tail nl        *)
function mkNamelist (nm: NAME; nl: NAMELIST): NAMELIST;

(* mkValuelist - return an VALUELIST with head n and tail vl     *)
function mkValuelist (n: NUMBER; vl: VALUELIST): VALUELIST;

(* mkEnv - return an ENV with vars nl and values vl              *)
function mkEnv (nl: NAMELIST; vl: VALUELIST): ENV;

(* lengthVL - return length of VALUELIST vl                      *)
function lengthVL (vl: VALUELIST): integer;

(* lengthNL - return length of NAMELIST nl                       *)
function lengthNL (nl: NAMELIST): integer;


(*****************************************************************
 *                     NAME MANAGEMENT                           *
 *****************************************************************)

(* fetchFun - get function definition of fname from fundefs      *)
function fetchFun (fname: NAME): FUNDEF;

(* newFunDef - add new function fname w/ parameters nl, body e   *)
procedure newFunDef (fname: NAME; nl: NAMELIST; e: EXP);

(* initNames - place all pre-defined names into printNames       *)
procedure initNames;

(* install - insert new name into printNames                     *)
function install (nm: NAMESTRING): NAME;

(* prName - print name nm                                        *)
procedure prName (nm: NAME);

(* primOp - translate NAME optr to corresponding BUILTINOP       *)
function primOp (optr: NAME): BUILTINOP;


(*****************************************************************
 *                        INPUT                                  *
 *****************************************************************)

(* isDelim - check if c is a delimiter                           *)
function isDelim (c: char): Boolean;

(* skipblanks - return next non-blank position in userinput      *)
function skipblanks (p: integer): integer;

(* matches - check if string nm matches userinput[s .. s+leng]   *)
function matches (s: integer; leng: NAMESIZE;

(* reader - read char's into userinput; be sure input not blank  *)
procedure reader;
   (* readInput - read char's into userinput                        *)
   procedure readInput;
      (* nextchar - read next char - filter tabs and comments          *)
      procedure nextchar (var c: char);
      (* readParens - read char's, ignoring newlines, to matching ')'  *)
      procedure readParens;

(* parseName - return (installed) NAME starting at userinput[pos]*)
function parseName: NAME;

(* isNumber - check if a number begins at pos                    *)
function isNumber (pos: integer): Boolean;
   (* isDigits - check if sequence of digits begins at pos          *)
   function isDigits (pos: integer): Boolean;

(* parseVal - return number starting at userinput[pos]           *)
function parseVal: NUMBER;

function parseEL: EXPLIST; forward;
(* parseExp - return EXP starting at userinput[pos]              *)

function parseExp: EXP;
var
   nm: NAME;
   el: EXPLIST;
begin
   if userinput[pos] = '('
   then begin   (* APEXP *)
           pos := skipblanks(pos+1); (* skip '( ..' *)
           nm := parseName;
           el := parseEL;
           parseExp := mkAPEXP(nm, el)
        end
   else if isNumber(pos)
        then parseExp := mkVALEXP(parseVal)   (* VALEXP *)
        else parseExp := mkVAREXP(parseName)  (* VAREXP *)
end; (* parseExp *)

(* parseEL - return EXPLIST starting at userinput[pos]           *)
function parseEL;

(* parseNL - return NAMELIST starting at userinput[pos]          *)
function parseNL: NAMELIST;

(* parseDef - parse function definition at userinput[pos]        *)
function parseDef: NAME;


(*****************************************************************
 *                     ENVIRONMENTS                              *
 *****************************************************************)

(* emptyEnv - return an environment with no bindings             *)
function emptyEnv: ENV;

(* bindVar - bind variable nm to value n in environment rho      *)
procedure bindVar (nm: NAME; n: NUMBER; rho: ENV);

(* findVar - look up nm in rho                                   *)
function findVar (nm: NAME; rho: ENV): VALUELIST;

(* assign - assign value n to variable nm in rho                 *)
procedure assign (nm: NAME; n: NUMBER; rho: ENV);

(* fetch - return number bound to nm in rho                      *)
function fetch (nm: NAME; rho: ENV): NUMBER;

(* isBound - check if nm is bound in rho                         *)
function isBound (nm: NAME; rho: ENV): Boolean;


(*****************************************************************
 *                     NUMBERS                                   *
 *****************************************************************)

(* prValue - print number n                                      *)
procedure prValue (n: NUMBER);

(* isTrueVal - return true if n is a true (non-zero) value       *)
function isTrueVal (n: NUMBER): Boolean;

(* applyValueOp - apply VALUEOP op to arguments in VALUELIST vl  *)
function applyValueOp (op: VALUEOP; vl: VALUELIST): NUMBER;
   (* arity - return number of arguments expected by op             *)
   function arity (op: VALUEOP): integer;
   (* ... *)

begin (* applyValueOp *)
   if arity(op) <> lengthVL(vl)
   then begin
           write('Wrong number of arguments to ');
           prName(ord(op)+1);
           writeln;
           goto 99
        end;
   n1 := vl^.head; (* 1st actual *)
   if arity(op) = 2 then n2 := vl^.tail^.head; (* 2nd actual *)
   case op of
      PLUSOP: n := n1+n2;
      MINUSOP: n := n1-n2;
      TIMESOP: n := n1*n2;
      DIVOP: n := n1 div n2;
      EQOP: if n1 = n2 then n := 1 else n := 0;
      LTOP: if n1 < n2 then n := 1 else n := 0;
      GTOP: if n1 > n2 then n := 1 else n := 0;
      PRINTOP:
         begin prValue(n1); writeln; n := n1 end
   end; (* case *)
   applyValueOp := n
end; (* applyValueOp *)


(*****************************************************************
 *                     EVALUATION                                *
 *****************************************************************)

(* eval - return value of expression e in local environment rho  *)
function eval (e: EXP; rho: ENV): NUMBER;

var op: BUILTINOP;

   (* evalList - evaluate each expression in el                     *)
   function evalList (el: EXPLIST): VALUELIST;
   (* applyUserFun - look up definition of nm and apply to actuals  *)
   function applyUserFun (nm: NAME; actuals: VALUELIST): NUMBER;
   (* applyCtrlOp - apply CONTROLOP op to args in rho               *)
   function applyCtrlOp (op: CONTROLOP;  args: EXPLIST): NUMBER;

begin (* eval *)
   with e^ do
      case etype of
         VALEXP:
            eval := num;
         VAREXP:
            if isBound(varble, rho)
            then eval := fetch(varble, rho)
            else if isBound(varble, globalEnv)
                 then eval := fetch(varble, globalEnv)
                 else begin
                         write('Undefined variable: ');
                         prName(varble);
                         writeln;
                         goto 99
                      end;
         APEXP: 
            if optr > numBuiltins
            then eval := applyUserFun(optr, evalList(args))
            else begin
                    op := primOp(optr);
                    if op in [IFOP .. BEGINOP]
                    then eval := applyCtrlOp(op, args)
                    else eval := applyValueOp(op,
                                     evalList(args))
                 end
      end (* case and with *)
end; (* eval *)

(*****************************************************************
 *                     READ-EVAL-PRINT LOOP                      *
 *****************************************************************)

begin (* chapter1 main *)
   initNames;
   globalEnv := emptyEnv;

   quittingtime := false;
99:
   while not quittingtime do begin
      reader;
      if matches(pos, 4, 'quit                ')
      then quittingtime := true
      else if (userinput[pos] = '(') and
              matches(skipblanks(pos+1), 6, 'define              ')
           then begin
                   prName(parseDef);
                   writeln
                end
           else begin
                   currentExp := parseExp;
                   prValue(eval(currentExp, emptyEnv));
                   writeln;
                   writeln
                end
      end (* while *)
end. (* chapter1 *)