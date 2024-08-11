#include "src/cppparser/CppParser.h"
#include <clang/AST/AST.h>
#include <clang/AST/RecursiveASTVisitor.h>
#include <clang/Frontend/FrontendActions.h>
#include <clang/Tooling/CommonOptionsParser.h>
#include <clang/Tooling/Tooling.h>

using namespace clang;
using namespace clang::tooling;

class MyASTVisitor : public RecursiveASTVisitor<MyASTVisitor>
{
  public:
    bool VisitFunctionDecl(FunctionDecl* f)
    {
        if (f->hasBody())
        {
            llvm::outs() << "Function name: " << f->getNameInfo().getName().getAsString() << "\n";
        }
        return true;
    }
};

class MyASTConsumer : public ASTConsumer
{
  public:
    virtual void HandleTranslationUnit(ASTContext& context)
    {
        MyASTVisitor visitor;
        visitor.TraverseDecl(context.getTranslationUnitDecl());
    }
};

class MyFrontendAction : public ASTFrontendAction
{
  public:
    virtual std::unique_ptr<ASTConsumer> CreateASTConsumer(CompilerInstance& CI, StringRef file)
    {
        return std::make_unique<MyASTConsumer>();
    }
};

static llvm::cl::OptionCategory MyToolCategory("my-tool options");

int ParseFile(const char* cppfile)
{
    // auto ExpectedParser = CommonOptionsParser::create(argc, argv, MyToolCategory);
    // if (!ExpectedParser)
    // {
    //     // Fail gracefully for unsupported options.
    //     llvm::errs() << ExpectedParser.takeError();
    //     return 1;
    // }
    // CommonOptionsParser& OptionsParser = ExpectedParser.get();
    // ClangTool            Tool(OptionsParser.getCompilations(), OptionsParser.getSourcePathList());

    return clang::tooling::runToolOnCode(std::make_unique<MyFrontendAction>(), cppfile);
}
