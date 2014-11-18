#Clockwork for Dynamo - Version History

##0.74.1

###New nodes:
- DividedSurface.HorizontalIntersectsByEndpoints
- DividedSurface.HorizontalIntersectsByEndpointsAnd Function
- DividedSurface.VerticalIntersectsByEndpoints
- DividedSurface.VerticalIntersectsByEndpointsAnd Function
- Document.SaveAs
- FamilyInstance.CopingElements
- FamilyInstance.AddCoping
- FamilyInstance.RemoveCoping
- List.ReplaceItemAtIndex
- PerspectiveView.SetOrientationByEyeAndTargetPosition
- Surface.IsPlanar
- Surface.Vertices
- UV.PruneDuplicates
- Vector.PruneDuplicates
- View3D.IsLocked

###Deprecated nodes:
- Directory.FromFilePath - Use Directory.FromPath instead
- Elements.RemoveDuplicates - Use List.UniqueItems instead (it will now remove duplicate Revit elements from a list as well)

##0.73.2

###New nodes:
- Document.DimensionTypes
- List.RandomElements
- Math.RandomIntegerList
- SelectionSet.ByElements
- TextNote.ByStringAndPosition

###Fixes:
- Element.Inserts now returns a single list of elements when fed a single element
- FamilyInstance.SetType now takes a list of types 

##0.73.1
First (more or less) complete edition for Dynamo 0.7.x

##0.63.3
First complete edition for Dynamo 0.6.3