using System.Globalization;
using System.Reflection;
using System.Security.Cryptography;
using System.Text;
using OriginalCircuit.Altium.Models.Pcb;
using OriginalCircuit.Altium.Models.Sch;
using OriginalCircuit.Altium.Serialization.Writers;
using OriginalCircuit.Altium.Serialization.Readers;
using OriginalCircuit.Eda.Primitives;
using PinOrientation = OriginalCircuit.Eda.Enums.PinOrientation;
using PinElectricalType = OriginalCircuit.Altium.Models.Sch.PinElectricalType;

var root = args.Length > 0 ? Path.GetFullPath(args[0]) : Directory.GetCurrentDirectory();
var output = Path.Combine(root,"Nativo_Altium");Directory.CreateDirectory(output);
const string symbolName="TWOTREES_TMC2209_V20";
const string footprintName="TWOTREES_TMC2209_V20_2X8";
const string stem="TWOTREES_TMC2209_V20";
Coord M(double mm)=>Coord.FromMm(mm);
CoordPoint XY(double x,double y)=>new(M(x),M(y));
var rows=File.ReadAllLines(Path.Combine(root,"pinagem.csv")).Skip(1).Where(s=>!string.IsNullOrWhiteSpace(s)).Select(s=>s.Split(',')).ToArray();
var pcb=new PcbLibrary();
var fp=PcbComponent.Create(footprintName).WithDescription("TWOTREES TMC2209 V2.0; 2x8 sockets; nominal mechanical study Rev B; blue heatsink embedded").WithHeight(M(22.315)).Build();
foreach(var r in rows){
 int n=int.Parse(r[0]);double x=double.Parse(r[2],CultureInfo.InvariantCulture),y=double.Parse(r[3],CultureInfo.InvariantCulture);
 var shape=n==1?PadShape.Rectangular:PadShape.Round;
 fp.AddPad(new PcbPad{Designator=r[0],Location=XY(x,y),SizeTop=XY(1.9,1.9),SizeMiddle=XY(1.9,1.9),SizeBottom=XY(1.9,1.9),HoleSize=M(1),IsPlated=true,Layer=74,ShapeTop=shape,ShapeMiddle=shape,ShapeBottom=shape,SolderMaskExpansion=M(.05)});
}
void Outline(double x,double y,int layer){
 var corners=new[]{XY(-x,-y),XY(x,-y),XY(x,y),XY(-x,y)};
 for(int i=0;i<4;i++)fp.AddTrack(new PcbTrack{Start=corners[i],End=corners[(i+1)%4],Width=M(.15),Layer=layer});
}
Outline(7.62,10.16,21);Outline(8.2,10.75,58);
fp.AddText(new PcbText{Text=".Designator",Location=XY(-7.62,11.5),Height=M(1),StrokeWidth=M(.15),Layer=21});
fp.AddText(new PcbText{Text="EN",Location=XY(-5.1,8),Height=M(.7),StrokeWidth=M(.1),Layer=21});
fp.AddText(new PcbText{Text="VM",Location=XY(3.8,8),Height=M(.7),StrokeWidth=M(.1),Layer=21});
var stepFile="TWOTREES_TMC2209_V20_Completo.step";
var stepBytes=File.ReadAllBytes(Path.Combine(root,stepFile));var modelId="{627B340D-0B33-41AA-B508-33A2CA91ED20}";
var checksum=PcbModel.ComputeChecksum(stepBytes);
pcb.Models.Add(new PcbModel{Id=modelId,Name=stepFile,IsEmbedded=true,StepData=Encoding.UTF8.GetString(stepBytes),Checksum=unchecked((int)checksum)});
var body=new PcbComponentBody{Name="TWOTREES V2.0 with heatsink and sockets",Kind=1,IsShapeBased=false,Layer=57,LayerName="MECHANICAL1",OverallHeight=M(22.315),StandoffHeight=M(0),ModelId=modelId,ModelName=stepFile,ModelEmbed=true,ModelType=1,ModelChecksum=checksum,BodyOpacity3D=1,Model2DLocation=XY(0,0),Model3DDz=M(0)};
body.SetOutline(new[]{XY(-7.62,-10.16),XY(7.62,-10.16),XY(7.62,10.16),XY(-7.62,10.16)});fp.AddComponentBody(body);pcb.Add(fp);
var sch=new SchLibrary();
var sym=new SchComponent{Name=symbolName,Description="TWOTREES TMC2209 V2.0 module, as photographed. PDN and USART separate; mechanical study Rev B.",PartCount=1,DesignatorPrefix="U"};
sym.AddRectangle(new SchRectangle{Corner1=XY(-12.7,-11.43),Corner2=XY(12.7,11.43),Color=128,FillColor=0xE8FFFF,IsFilled=true,LineWidth=M(.254),OwnerPartId=1});
foreach(var r in rows){
 int n=int.Parse(r[0]);string name=r[1];double y=double.Parse(r[3],CultureInfo.InvariantCulture);
 var type=name.StartsWith("GND")||name=="VM"||name=="VIO"?PinElectricalType.Power:name is "PDN" or "USART"?PinElectricalType.Passive:name.StartsWith("M1")||name.StartsWith("M2")?PinElectricalType.Output:PinElectricalType.Input;
 sym.AddPin(new SchPin{Designator=r[0],Name=name,Location=XY(n<=8?-17.78:17.78,y),Length=M(5.08),Orientation=n<=8?PinOrientation.Right:PinOrientation.Left,ElectricalType=type,ShowName=true,ShowDesignator=true,OwnerPartId=1});
}
sym.AddParameter(new SchParameter{Name="Designator",Value="U?",Location=XY(-12.7,13.97),IsVisible=true,OwnerPartId=1});
sym.AddParameter(new SchParameter{Name="Comment",Value=symbolName,Location=XY(-12.7,-15.24),IsVisible=true,OwnerPartId=1});
sym.AddParameter(new SchParameter{Name="MechanicalStatus",Value="NOMINAL_DIMENSIONS_VERIFY_PHYSICAL_MODULE",IsVisible=false,OwnerPartId=1});
var impl=new SchImplementation{ModelName=footprintName,ModelType="PCBLIB",Description="Native PcbLib footprint with embedded STEP",IsCurrent=true,OwnerPartId=1};
impl.DataFileKinds.Add("PCBLib");impl.DataFileEntities.Add(footprintName);
// Authoring methods are internal in this pinned upstream API. Explicit 1:1 mapping.
var addMap=typeof(SchImplementation).GetMethod("AddMapDefiner",BindingFlags.Instance|BindingFlags.NonPublic)!;
foreach(var r in rows){var map=new SchMapDefiner{DesignatorInterface=r[0],IsTrivial=true,OwnerPartId=1};map.DesignatorImplementations.Add(r[0]);addMap.Invoke(impl,new object[]{map});}
typeof(SchComponent).GetMethod("AddImplementation",BindingFlags.Instance|BindingFlags.NonPublic)!.Invoke(sym,new object[]{impl});sch.Add(sym);
var pcbPath=Path.Combine(output,stem+".PcbLib");var schPath=Path.Combine(output,stem+".SchLib");
await new PcbLibWriter().WriteAsync(pcb,pcbPath,overwrite:true);
await new SchLibWriter().WriteAsync(sch,schPath,overwrite:true);
// Read from the files, not the source models, and check all 16 positions and associations.
var pcbRead=await new PcbLibReader().ReadAsync(pcbPath);var schRead=await new SchLibReader().ReadAsync(schPath);
void Check(bool test,string message){if(!test)throw new Exception("FAIL: "+message);Console.WriteLine("PASS: "+message);}
Check(pcbRead.Components.Count==1&&schRead.Components.Count==1,"one native footprint and one native schematic symbol");
var fpr=(PcbComponent)pcbRead.Components[0];var sr=(SchComponent)schRead.Components[0];
Check(fpr.Pads.Count==16&&sr.Pins.Count==16,"16 through-hole pads and 16 symbol pins");
foreach(var r in rows){
 var pad=fpr.Pads.Single(p=>p.Designator==r[0]);var pin=sr.Pins.Single(p=>p.Designator==r[0]);
 Check(pin.Name==r[1]&&pad.Location==XY(double.Parse(r[2],CultureInfo.InvariantCulture),double.Parse(r[3],CultureInfo.InvariantCulture))&&pad.HoleSize==M(1)&&pad.Layer==74,"pin/pad "+r[0]+" = "+r[1]+"; position, drill, multi-layer");
}
Check(sr.Implementations.Count==1&&sr.Implementations[0].ModelName==footprintName&&sr.Implementations[0].ModelType=="PCBLIB","symbol linked to footprint");
Check(sr.Implementations[0].MapDefiners.Count==16&&sr.Implementations[0].MapDefiners.All(m=>m.DesignatorImplementations.Single()==m.DesignatorInterface),"all 16 pin-to-pad associations are 1:1");
Check(pcbRead.Models.Count==1&&Encoding.UTF8.GetBytes(pcbRead.Models[0].StepData).SequenceEqual(stepBytes),"embedded STEP bytes match original model");
Check(fpr.ComponentBodies.Count==1&&((PcbComponentBody)fpr.ComponentBodies[0]).ModelId==pcbRead.Models[0].Id,"3D body references embedded model");
foreach(var path in new[]{pcbPath,schPath})Check(File.ReadAllBytes(path).Take(8).SequenceEqual(Convert.FromHexString("D0CF11E0A1B11AE1")),Path.GetExtension(path)+" has native OLE compound-file header");
foreach(var d in pcbRead.Diagnostics.Concat(schRead.Diagnostics))Console.WriteLine("READER DIAGNOSTIC: "+d);
Console.WriteLine("Altium GUI validation and physical dimensional verification remain pending.");
