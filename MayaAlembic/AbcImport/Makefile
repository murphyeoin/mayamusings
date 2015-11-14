#-
# ==========================================================================
# Copyright (c) 2011 Autodesk, Inc.
# All rights reserved.
# 
# These coded instructions, statements, and computer programs contain
# unpublished proprietary information written by Autodesk, Inc., and are
# protected by Federal copyright law. They may not be disclosed to third
# parties or copied or duplicated in any form, in whole or in part, without
# the prior written consent of Autodesk, Inc.
# ==========================================================================
#+

ifndef INCL_BUILDRULES

#
# Include platform specific build settings
#
TOP := /home/eoin/Documents/mayamusings/MayaAlembic
include $(TOP)/buildrules



#
# Always build the local plug-in when make is invoked from the
# directory.
#
all : prebuiltPlugins

endif

#
# Variable definitions
#

SRCDIR := $(TOP)/AbcImport
OBJDIR := $(TOP)/AbcImport
DSTDIR := $(TOP)/AbcImport/build


AbcImport_SOURCES  := $(SRCDIR)/AbcImport.cpp $(SRCDIR)/AbcImportStrings.cpp $(SRCDIR)/AlembicNode.cpp $(SRCDIR)/CreateSceneHelper.cpp $(SRCDIR)/main.cpp $(SRCDIR)/MeshHelper.cpp $(SRCDIR)/NodeIteratorVisitorHelper.cpp $(SRCDIR)/PointHelper.cpp $(SRCDIR)/util.cpp $(SRCDIR)/XformHelper.cpp $(SRCDIR)/CameraHelper.cpp $(SRCDIR)/NurbsCurveHelper.cpp $(SRCDIR)/LocatorHelper.cpp $(SRCDIR)/NurbsSurfaceHelper.cpp $(SRCDIR)/AlembicImportFileTranslator.cpp
AbcImport_OBJECTS  := $(OBJDIR)/AbcImport.o $(OBJDIR)/AbcImportStrings.o $(OBJDIR)/AlembicNode.o $(OBJDIR)/CreateSceneHelper.o $(OBJDIR)/main.o $(OBJDIR)/MeshHelper.o $(OBJDIR)/NodeIteratorVisitorHelper.o $(OBJDIR)/PointHelper.o $(OBJDIR)/util.o  $(OBJDIR)/XformHelper.o $(OBJDIR)/CameraHelper.o $(OBJDIR)/NurbsCurveHelper.o $(OBJDIR)/LocatorHelper.o $(OBJDIR)/NurbsSurfaceHelper.o $(OBJDIR)/AlembicImportFileTranslator.o
AbcImport_PLUGIN   := $(DSTDIR)/AbcImport.$(EXT)
AbcImport_MAKEFILE := $(DSTDIR)/Makefile

#
# Include the optional per-plugin Makefile.inc
#
#    The file can contain macro definitions such as:
#       {pluginName}_EXTRA_CFLAGS
#       {pluginName}_EXTRA_C++FLAGS
#       {pluginName}_EXTRA_INCLUDES
#       {pluginName}_EXTRA_LIBS
-include $(SRCDIR)/Makefile.inc



#
# Set target specific flags.
#

$(AbcImport_OBJECTS): CFLAGS   := $(CFLAGS)   $(AbcImport_EXTRA_CFLAGS)
$(AbcImport_OBJECTS): C++FLAGS := $(C++FLAGS) $(AbcImport_EXTRA_C++FLAGS)
$(AbcImport_OBJECTS): INCLUDES := $(INCLUDES) $(AbcImport_EXTRA_INCLUDES)

depend_AbcImport:     INCLUDES := $(INCLUDES) $(AbcImport_EXTRA_INCLUDES)

$(AbcImport_PLUGIN):  LFLAGS   := $(LFLAGS) $(AbcImport_EXTRA_LFLAGS) 
$(AbcImport_PLUGIN):  LIBS     := $(LIBS)   -lOpenMaya -lFoundation -lOpenMayaAnim -lOpenMayaFX -lOpenMayaRender -lOpenMayaUI -lAlembicAbcCoreFactory -lAlembicAbcCoreHDF5 -lAlembicAbcCoreOgawa -lAlembicAbcGeom -lAlembicAbc -lAlembicAbcCoreAbstract -lAlembicAbcMaterial -lAlembicAbcCollection -lAlembicOgawa -lAlembicUtil -lhdf5_hl -lhdf5 -lAlembicIex -lAlembicHalf -lAlembicImath -lz $(AbcImport_EXTRA_LIBS) 

#
# Rules definitions
#

.PHONY: clean_AbcImport Clean_AbcImport

%.ox :	%.cpp
	$(C++) -c $(INCLUDES) $(C++FLAGS) $< -o $@

$(AbcImport_PLUGIN): $(AbcImport_OBJECTS) 
	-rm -f $@
	$(LD) -o $@ $(LFLAGS) $^ $(LIBS)


clean_AbcImport:
	-rm -f $(AbcImport_OBJECTS)

Clean_AbcImport:
	-rm -f $(AbcImport_MAKEFILE).bak $(AbcImport_OBJECTS) $(AbcImport_PLUGIN)


prebuiltPlugins: $(AbcImport_PLUGIN)
clean:	 clean_AbcImport
Clean:	 Clean_AbcImport

